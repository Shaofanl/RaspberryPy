import os
import sys
import subprocess


class Cell(object):
  def __init__(self, content):
    self.content = content
  @property
  def name(self):
    return self.truncate('ESSID:')[1:-1] 
  @property
  def quality(self):
    return (lambda q: float(q[0])/float(q[1])*100)\
                      (self.truncate('Quality=', endding=' ').split('/'))
  @property
  def siglevel(self):
    return int( self.truncate('Signal level=', endding=' dBm') )

  def __repr__(self):
    return '<Cell: name={} quality={}>'.format(self.name, self.quality)

  def truncate(self, key, length=None, endding='\n'):
    try:
      line = self.content
      start = line.index(key)+len(key)
      line = line[start:]
      return line[:length].split(endding, 1)[0]
    except:
      return None

class Wifi(object):
  def __init__(self, interface, ignore_root_limit=False):
    if not ignore_root_limit:
      if os.getuid() != 0:
        raise Exception("Wifi module should run with root permisson. To ignore that, please set ignore_root_limit=True")
    self.interface = interface
    self.update()

  def update(self):
    proc = subprocess.Popen(["iwlist", self.interface, "scan"],
                          universal_newlines=True,
                          stdout=subprocess.PIPE,) 
    out, err = proc.communicate()
 
    self.cells = dict(map(lambda x: (x.name, x), 
                          map(Cell, out.split('Cell')[1:])))



