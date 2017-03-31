from raspberrypy.sensor.HC_SR04 import HC_SR04
from time import sleep, time

if __name__ == '__main__':
  sensor1 = HC_SR04(trig=13, echo=15)
  sensor2 = HC_SR04(trig=16, echo=18)

  while True:
    sleep(0.5)
    print (sensor1.get_dis(), sensor2.get_dis())
  
