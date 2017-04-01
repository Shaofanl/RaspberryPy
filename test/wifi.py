import sys
sys.path.insert(0, './')
from raspberrypy.utils.wifi import Wifi
from time import sleep

if __name__ == '__main__':
  wifi = Wifi(interface='wlan0', ignore_root_limit=True)

  def get_pos(wifi):
    wifi.update()
    return (wifi.cells['CandyTime_804_plus'].siglevel,  
            wifi.cells['CandyTime_804'].siglevel)

  while True:
    sleep(0.5)
    print get_pos(wifi)

