from raspberrypy.display.LCD1602 import LCD1602A
from time import sleep

if __name__ == '__main__':
  lcd = LCD1602A()
  lcd.init()
  lcd.function_set(DL=0, N=1, F=0) # 2-line
  lcd.display(D=1, C=1, B=1)
  lcd.entry_mode(I_D=1, S=0)
  lcd.clear()
  lcd.set_line(line=0)
  lcd.write_msg("Hi")
  print 'done'
  
# lcd.lcd_cmd(0x33) # $33 8-bit mode   
# lcd.lcd_cmd(0x32) # $32 8-bit mode   
# lcd.lcd_cmd(0x28) # $28 8-bit mode   
# lcd.lcd_cmd(0x0C) # $0C 8-bit mode   
# lcd.lcd_cmd(0x06) # $06 8-bit mode   
# lcd.lcd_cmd(0x01) # $01 8-bit mode   
# lcd.lcd_string("Hello Pi")
# lcd.lcd_cmd(0xC0) # next line
# lcd.lcd_string("Forum peeps!")

  print 'done'

