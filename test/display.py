from raspberrypy.display.LCD1602 import LCD1602A
from time import sleep

if __name__ == '__main__':
    lcd = LCD1602A()
#   lcd.function_set(N=0, F=0) # 1-line, 5x8 dots
#   lcd.function_set(N=0, F=1) # 1-line, 5x11 dots


    lcd.function_set(DL=0, N=1, F=0) # 2-line
    lcd.entry_mode(S=0, I_D=1)
    lcd.display(D=1, C=1, B=1)
#   lcd.clear()

    lcd.write_msg("Hi", line=0)
    print 'done'

