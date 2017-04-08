from ..utils.GPIO_utils import setup_output, output, GPIO_Base
import RPi.GPIO as GPIO
from time import sleep

class LCD1602A(GPIO_Base):
    '''
        Vss: 0V
        Vdd: 5V
        Contrast: 0V
        RS: register select: H:Data Input L:instruction Input
        RW: read write: H:Read L:Write
        EN: enable Signal 
        DB: data bus
          DB0~DB3: data bus used in 8 bit transfer
          DB4~DB7: data bus for both 4 and 8 bit transfer
        BLA: black ground light +5V
        BLK: black ground light +0V

        currently we use a 4-bit bus mode 
            since there is not enough pins on raspberry pi
    '''

    T_DSW = 1e-4 # Data setup write (> 40 ns = 1e-8 s)
    T_PW  = 1e-4 # Enable plus width (> 140 ns = 1.4e-7 ns)
    T_R   = 1e-4 # Enable Rise Time (< 25 ns = 2.5e-8 ns)
    T_F   = 1e-4 # Enable Fall Time (< 25 ns = 2.5e-8 ns)
    T_C   = 1e-4 # Enable cycle (> 1200 ns = 1.2e-6 ns)
    def __init__(self, RS=7, RW=11, EN=12, DB=[29, 31, 32, 33], **kwargs):
        super(LCD1602A, self).__init__(**kwargs)

        self.RS = RS 
        self.RW = RW
        self.EN = EN
        self.DB = DB # DB4,5,6,7
        assert len(self.DB) == 4, 'Currently only 4-bit bus mode is supported'

        setup_output(RS)
        setup_output(RW)
        setup_output(EN)
        [setup_output(db) for db in DB if db is not None]

    # following operations is from https://www.openhacks.com/uploadsproductos/eone-1602a1.pdf
    def get_byte(self, *data):
        return  0b10000000*data[0]+\
                0b01000000*data[1]+\
                0b00100000*data[2]+\
                0b00010000*data[3]+\
                0b00001000*data[4]+\
                0b00000100*data[5]+\
                0b00000010*data[6]+\
                0b00000001*data[7]

    def output(self, rs, rw, data):
        ''' RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0 '''
        output(self.RS, rs)
        output(self.RW, rw)
        # higher bits
        output(self.DB[0], data&0b00010000 != 0)
        output(self.DB[1], data&0b00100000 != 0)
        output(self.DB[2], data&0b01000000 != 0)
        output(self.DB[3], data&0b10000000 != 0)
        self.establish()
        # lower bits (4-bit bus mode)
        output(self.DB[0], data&0b00000001 != 0)
        output(self.DB[1], data&0b00000010 != 0)
        output(self.DB[2], data&0b00000100 != 0)
        output(self.DB[3], data&0b00001000 != 0)
        self.establish()

    def establish(self):
        sleep(self.T_F)
        output(self.EN, 1)
        sleep(self.T_PW)
        output(self.EN, 0)

    def function_set(self, DL=0, N=1, F=0):
        '''
            RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
             0  0   0   0   1  DL   N   F  x   x

                 High    / Low
            DL: 8-bit    /4-bit
             N: 2-line   /1-line 
             F: 5x11 dots/5x8 dots
        '''
        self.output(rs=0, rw=0, data=self.get_byte(0,0,1,DL,N,F,0,0))

    def clear(self):
        self.output(rs=0, rw=0, data=self.get_byte(0,0,0,0,0,0,0,1))

    def return_home(self):
        self.output(rs=0, rw=0, data=self.get_byte(0,0,0,0,0,0,1,0))

    def entry_mode(self, I_D=1, S=0):
        '''
            RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
             0  0  0   0   0   0   0   1  I_D  S

            I_D: 1 cursor move to right and DDRAM address is increased by 1
                 0 cursor move to left and DDRAM address is decreased by 1

            S   I_D
            1   1       shift the display to the left
            1   0       shift the display to the right 
        '''
        self.output(rs=0, rw=0, data=self.get_byte(0,0,0,0,0,1,I_D,S))

    def display(self, D=1, C=0, B=0):
        '''
            RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
             0  0  0   0   0   0   1   D   C   B

             D: display     / no display
             C: cursor      / no cursor
             B: blink       / no blink
        '''
        self.output(rs=0, rw=0, data=self.get_byte(0,0,0,0,1,D,C,B))

    def cursor_shift(self, S_C, R_L):
        '''
            RS RW DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0
             0  0  0   0   0   1  S_C R_L  x   x

            S_C R_L
             0   0      shift cursor to the left                                        AC=AC-1
             0   1      shift curosr to the right                                       AC=AC+1
             1   0      shift display to the left. cursor follows the display shift     AC=AC
             1   1      shift display to the right. cursor follows the display shift    AC=AC
        '''
        pass

    def write_msg(self, msg, line=0):
        msg = msg.ljust(16, " ")[:16]
        print "[",msg,"]"

        # LCD_LINE_0 = 0x80, 0b1000 0000
        # LCD_LINE_1 = 0xC0, 0b1101 0000

        # one-line mode: 0x00~0x4F 
        # two-line mode: 0x00~0x27 + 0x40~67H
        self.output(rs=0, rw=0, data=0b10000000)#+(0x00 if line == 0 else 0x40))
        for char in msg:
            self.output(rs=1, rw=0, data=ord(char))


