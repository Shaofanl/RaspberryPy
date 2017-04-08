from ..utils.GPIO_utils import setup_input, fetch, GPIO_Base
 

class GY521(GPIO_Base):
    '''
        MPU6050(GY521)

        install the I2C dev
            sudo apt-get install libi2c-dev
        install smbus
            sudo apt-get isntall python-smbus
        enable i2c
            Old version:
                sudo raspi-config
                7 advanced options
                A7 I2C  (if this options not exist, update your raspi-config first)
                Enable 
            New version:
                sudo raspi-config 
                5 Interfacing Options
                P5 I2C
                Enable
        check which port the GY521 is on 
            i2cdetect -y 1 # switch 1 to 0 if the 0x68 is not exist
    '''
    def __init__(self, **kwargs):
        super(GY521, self).__init__(**kwargs)
    
