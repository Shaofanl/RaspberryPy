from ..utils.GPIO_utils import setup_input, setup_output, \
                fetch, update, GPIO_Base
from time import sleep, time

class HC_SR04(GPIO_Base):
  ''' HC_SR04 ultrasonic '''
  def __init__(self, trig=16, echo=18, calibration=0.5, **kwargs):
    super(HC_SR04, self).__init__(**kwargs)
    self.trig = trig
    self.echo = echo 
    self.calibration = calibration
    setup_output(trig)
    setup_input(echo)
  
  def get_dis(self, verbose=0):
#   update(self.trig, 0) 
#   if verbose > 0: print "Waitng For Sensor To Settle"
#   sleep(2.0)           # Delay 
    update(self.trig, 1)
    sleep(0.000015)       # keep > 10 us of high
    update(self.trig, 0)
  
    while fetch(self.echo) == 0: pass
    pulse_start = time() 
    while fetch(self.echo) == 1: pass
    pulse_duration = time() - pulse_start 
  
    dis = pulse_duration * 17150   # time/2.0*340 M/s (the speed of sound forward and backward)
    dis = round(dis, 2)
  
    if dis > 2 and dis < 400:   
      return dis - self.calibration
    else:
      if verbose>0: print "Out Of Range"                 
      return -1

