#!/usr/bin/python

# read IP and display on the LCD
# netifaces required
# add to /etc/rc.local to autorun 

from raspberrypy.display.LCD1602 import LCD1602A 
from time import sleep
import netifaces as ni

if __name__ == '__main__':
  lcd = LCD1602A()

  lcd.init()
  lcd.function_set(DL=0, N=1, F=0) # 2-line
  lcd.display(D=1, C=1, B=1)
  lcd.entry_mode(I_D=1, S=0)
  lcd.set_interval(1e-2)

  for interface in ['eth0', 'wlan0']: 
    try:
      ip = ni.ifaddresses(interface)[2][0]['addr']

      lcd.set_line(line=0)
      lcd.printf("IP of "+interface+":")
      lcd.set_line(line=1)
      lcd.printf(ip)
      break
    except:
      lcd.set_line(line=0)
      lcd.printf("IP of "+interface+":")
      lcd.set_line(line=1)
      lcd.printf("does not exist.")
