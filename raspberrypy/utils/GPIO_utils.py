import RPi.GPIO as GPIO
from time import sleep

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

# output signal
def low(pin):
  GPIO.output(pin, GPIO.LOW)
def high(pin):
  GPIO.output(pin, GPIO.HIGH)
def update(pins, outputs):
  for pin, output in zip(pins, outputs):
    GPIO.output(pin, output)

