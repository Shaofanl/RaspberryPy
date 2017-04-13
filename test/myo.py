from __future__ import print_function

import sys, time
from raspberrypy.control.myo import Myo

if __name__ == '__main__':
  m = Myo(sys.argv[1] if len(sys.argv) >= 2 else None)

  def proc_emg(emg, moving, times=[]):
    print(emg)

    ## print framerate of received data
    times.append(time.time())
    if len(times) > 20:
      #print((len(times) - 1) / (times[-1] - times[0]))
      times.pop(0)

# m.add_emg_handler(proc_emg)
  m.connect()

  m.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
  m.add_pose_handler(lambda p: print('pose', p))

  try:
    while True:
      m.run(1)

  except KeyboardInterrupt:
    pass
  finally:
    m.disconnect()
    print()
