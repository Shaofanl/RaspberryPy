from raspberrypy.control.myo import Myo, Pose
from raspberrypy.motor.L289N import L289N

if __name__ == '__main__':
  motor = L289N()
  myo   = Myo()


  def changeMotorOnPose(pose):
    print pose
    if pose == Pose.REST:
      motor.stop()
    elif pose == Pose.FIST:
      motor.forward(-1)
    elif pose == Pose.WAVE_IN:
      motor.spin_left(-1)
    elif pose == Pose.WAVE_OUT:
      motor.spin_right(-1)
    elif pose == Pose.FINGERS_SPREAD:
      motor.backward(-1)
    else: 
      pass

  myo.add_pose_handler(changeMotorOnPose)


  myo.connect()
  try:
    while True: 
      myo.run(1)
  except KeyboardInterrupt:
    pass
  finally:
    myo.disconnect()
