#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# read information from GY521 and display on LCD1602

from raspberrypy.sensor.GY521 import GY521
from raspberrypy.display.LCD1602 import LCD1602A 
from time import sleep

if __name__ == '__main__': 
  gy = GY521()
  lcd = LCD1602A()

  lcd.init()
  lcd.function_set(DL=0, N=1, F=0) # 2-line
  lcd.display(D=1, C=1, B=1)
  lcd.entry_mode(I_D=1, S=0)
  lcd.set_interval(1e-4)

  while True:
    sleep(3.0)
    res = gy.get_all_data()

    lcd.clear()
    lcd.set_line(line=0)
    lcd.printf("ACC: {:+03.0f} {:+03.0f} {:+03.0f}".format(res['accel'].x, res['accel'].y, res['accel'].z)) 
               #01234  567    8   901   2   345
    lcd.set_line(line=1)
    lcd.printf("GYO: {:+03.0f} {:+03.0f} {:+03.0f}".format(res['gyro'].x, res['gyro'].y, res['gyro'].z)) 
