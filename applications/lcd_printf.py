#!/usr/bin/python

# link it to /usr/local/bin so that it can be executed from command line

from raspberrypy.display.LCD1602 import LCD1602A 
import sys

if __name__ == '__main__':
  lcd = LCD1602A()

  lcd.init()
  lcd.function_set(DL=0, N=1, F=0) # 2-line
  lcd.display(D=1, C=1, B=1)
  lcd.entry_mode(I_D=1, S=0)
  lcd.set_interval(1e-2)


  args = sys.argv[1:]
  print args
  for i in range(0, len(args), 2):
    lcd.set_line(line=int(args[i]))
    lcd.printf(args[i+1])

