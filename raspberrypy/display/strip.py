# install Neopixel for raspberry pi 
#   https://learn.adafruit.com/neopixels-on-raspberry-pi/software

try:
  import neopixel
  from neopixel import Color
except:
  raise ImportError("Please install Neopixel first (https://learn.adafruit.com/neopixels-on-raspberry-pi/software")
import time
import os

# ['Adafruit_NeoPixel', 
#  'Color', 
#  '_LED_Data', 
#  'atexit', 'ws',
#  '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__']

class Strip(neopixel.Adafruit_NeoPixel):
  def __init__(self,
    LED_COUNT      = 16,      # Number of LED pixels.
    LED_PIN        = 18,      # GPIO pin connected to the pixels (must support PWM!).
    LED_FREQ_HZ    = 800000,  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 5,       # DMA channel to use for generating signal (try 5)
    LED_INVERT     = False,   # True to invert the signal (when using NPN transistor level shift)
    LED_BRIGHTNESS = 255,     # Set to 0 for darkest and 255 for brightest
    ):
    super(Strip, self).__init__(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    if os.getuid() != 0:
      raise Exception("Neopixel module should run with root permisson.")
    self.begin()

  def setPattern(self, colors):
    assert len(colors) == self.numPixels()

    for i, c in enumerate(colors):
      self.setPixelColor(i, c)
      self.show()


  def pattern_wipe(self, color, wait_ms=50):
    for i in range(self.numPixels()):
      self.setPixelColor(i, color)
      self.show()
      time.sleep(wait_ms/1000.0)

  def pattern_chase(self, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
      for q in range(3):
        for i in range(0, self.numPixels(), 3):
          self.setPixelColor(i+q, color)
        self.show()
        time.sleep(wait_ms/1000.0)
        for i in range(0, self.numPixels(), 3):
          self.setPixelColor(i+q, 0)

  @staticmethod
  def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
      return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
      pos -= 85
      return Color(255 - pos * 3, 0, pos * 3)
    else:
      pos -= 170
      return Color(0, pos * 3, 255 - pos * 3)

  def rainbow(self, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
      for i in range(self.numPixels()):
        self.setPixelColor(i, self.wheel((i+j) & 255))
      self.show()
      time.sleep(wait_ms/1000.0)

  def rainbow(self, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
      for i in range(self.numPixels()):
        self.setPixelColor(i, self.wheel((i+j) & 255))
      self.show()
      time.sleep(wait_ms/1000.0)


