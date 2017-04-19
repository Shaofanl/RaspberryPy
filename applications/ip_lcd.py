#!/usr/bin/python

# read IP and display on the LCD
# netifaces required

from raspberrypy.display.LCD1602 import LCD1602A 
import netifaces as ni

if __name__ == '__main__':
  lcd = LCD1602A()

  lcd.init()
  lcd.clear()
  lcd.function_set(DL=0, N=1, F=0) # 2-line
  lcd.display(D=1, C=1, B=1)
  lcd.entry_mode(I_D=1, S=0)
  lcd.set_interval(1e-4)

  try:
    ni.ifaddresses('eth0')
    ip = ni.ifaddresses('eth0')[2][0]['addr']

    lcd.set_line(line=0)
    lcd.printf("IP:")
    lcd.set_line(line=1)
    lcd.printf(ip)
  except:
    lcd.set_line(line=0)
    lcd.printf("IP of eth0 not exists.")
