#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# read information from GY521 and display on LCD1602

from raspberrypy.sensor.GY521 import GY521
from raspberrypy.display.LCD1602 import LCD1602A 
from raspberrypy.utils.math import Vec3
from time import sleep, time

if __name__ == '__main__': 
  gy = GY521()
  lcd = LCD1602A()

  lcd.init()
  lcd.function_set(DL=0, N=1, F=0) # 2-line
  lcd.display(D=1, C=1, B=1)
  lcd.entry_mode(I_D=1, S=0)
  lcd.set_interval(1e-4)

  starter = time()
  acc_acc = Vec3(0, 0, 0)
  gyo_acc = Vec3(0, 0, 0)
  cnt = 0
  while True:
    if time() - starter > 1:
      acc_acc = acc_acc/cnt
      gyo_acc = gyo_acc/cnt

      lcd.clear()
      lcd.set_line(line=0)
      lcd.printf("ACC: {:+03.0f} {:+03.0f} {:+03.0f}".format(acc_acc.x, acc_acc.y, acc_acc.z)) 
                 #01234  567    8   901   2   345
      lcd.set_line(line=1)
      lcd.printf("GYO: {:+03.0f} {:+03.0f} {:+03.0f}".format(gyo_acc.x, gyo_acc.y, gyo_acc.z)) 

      starter = time()
      acc_acc = Vec3(0, 0, 0)
      gyo_acc = Vec3(0, 0, 0)
      cnt = 0

    res = gy.get_all_data()
    acc_acc = acc_acc + Vec3(res['accel'].x, res['accel'].y, res['accel'].z)
    gyo_acc = gyo_acc + Vec3(res['gyro'].x, res['gyro'].y, res['gyro'].z) 
    cnt += 1 
