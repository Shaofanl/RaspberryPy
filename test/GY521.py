from raspberrypy.sensor.GY521 import GY521

if __name__ == '__main__':
    gy = GY521()
    while True:
        print gy.get_all_data()
