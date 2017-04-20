from raspberrypy.motor.L289N import L289N
from raspberrypy.sensor.HC_SR04 import HC_SR04
from multiprocessing import Process, Value
from time import sleep
from random import random 
from raspberrypy.utils.GPIO_utils import cleanup_atexit

# constants
INTERVAL = 1e-3
SAMPLE_L = 20
STABLE_T = INTERVAL*SAMPLE_L*10
SAFE_DIS = 30
STEP     = 0.3

# objects
motor = L289N()
sensor1 = HC_SR04(trig=13, echo=15)
sensor2 = HC_SR04(trig=16, echo=18)

# value
dis_1 = Value('d', 0.0)
dis_2 = Value('d', 0.0)

# process
def F_proc_dis(d1, d2):
  samples1, samples2 = [], []
  s1, s2 = 0.0, 0.0
  while 1:
    s1 = sensor1.get_dis()
    s2 = sensor2.get_dis()
    samples1.append(s1 if s1 > 0 else samples1[-1])
    samples2.append(s2 if s2 > 0 else samples2[-1])

    samples1 = samples1[-SAMPLE_L:]  
    samples2 = samples2[-SAMPLE_L:]  

    d1.value = float(sum(samples1))/SAMPLE_L
    d2.value = float(sum(samples2))/SAMPLE_L
    sleep(INTERVAL)
proc_dis = Process(target=F_proc_dis, args=(dis_1, dis_2))


if __name__ == '__main__':
  cleanup_atexit()
  proc_dis.start()

  while 1:
    sleep(STABLE_T)
    print dis_1.value, dis_2.value
    if dis_1.value > SAFE_DIS and dis_2.value > SAFE_DIS:
      motor.forward(STEP)
    else:
      if random() < 0.5:
        motor.spin_left(STEP)
      else:
        motor.spin_right(STEP)
        
