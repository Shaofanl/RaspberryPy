from raspberrypy.display.strip import Strip, Color
from raspberrypy.utils.math import Vec3
from datetime import datetime
from time import sleep
from math import exp

def update(strip, colors):
  strip.setPattern(map(lambda x: Color(*x), colors))

if __name__ == '__main__':
  strip = Strip()
  n = strip.numPixels()
  colors = [Vec3(0,0,0) for i in range(n)]
  delay = 0 # 1e-1 
  handle = lambda a, b: int(abs(a-b)<=1.0/n or abs(a-b+1)<=1.0/n)

  while True:
    sleep(delay)
    update(strip, colors)

    t = datetime.now()
    second = t.second/60.

    colors = [Vec3(0,0,0) for i in range(n)]
    for i in range(n):
      ratio = float(i)/n
      diff  = handle(second, ratio)
      
      colors[i] = Vec3(0,0,int(255*diff))

    update(strip, colors)

