import RPi.GPIO as GPIO
from time import sleep

def cleanup_atexit():
  import atexit
  atexit.register(GPIO.cleanup)

def cleanup():
  GPIO.cleanup()

# mode
def get_mode_from_str(mode):
  if mode == 'BOARD': return GPIO.BOARD
  elif mode == 'BCM': return GPIO.BCM
  else: raise NotImplemented
def set_mode(mode):
  if isinstance(mode, str):
    GPIO.setmode(get_mode_from_str(mode))
  else:
    GPIO.setmode(mode)

# setup phase
def setup_output(pin):
  GPIO.setup(pin, GPIO.OUT)
def setup_input(pin):
  GPIO.setup(pin, GPIO.IN)

# input signal
def fetch(pin):
  return GPIO.input(pin)

# output signal
def low(pin):
  GPIO.output(pin, GPIO.LOW)
def high(pin):
  GPIO.output(pin, GPIO.HIGH)
def output(pin, output):
  if isinstance(pin, list): 
    for p, o in zip(pin, output):
      GPIO.output(p, o)
  else:
    GPIO.output(pin, output)

class GPIO_Base(object):
  def __init__(self, mode='BOARD'):
    if GPIO.getmode() is None:
      print 'Setting GPIO mode to {}.'.format(mode)
      self.mode = mode
      set_mode(mode)
    else:
      print 'GPIO mode {} exists.'.format(GPIO.getmode())
      
  def __del__(self):
    pass
    #print 'Cleaning up GPIO.'
    #cleanup()

