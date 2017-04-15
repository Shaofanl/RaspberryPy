from raspberrypy.motor.L289N import L289N
from time import sleep

if __name__ == '__main__':
  motor = L289N()
  print motor
# motor.left_forward(0.5)
# motor.right_forward(0.5)
# motor.right_backward(0.5)
# motor.left_backward(0.5)
  motor.spin_left(0.3)
  motor.stop(0.5)
  motor.spin_right(0.3)
# motor.forward(0.5)
# motor.backward(0.5)
