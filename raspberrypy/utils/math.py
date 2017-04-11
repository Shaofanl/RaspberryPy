class Vec3(object):
  def __init__(self, *data):
    if len(data) == 1: data = data[0]
    if isinstance(data, list) or isinstance(data, tuple):
      self.x = data[0]
      self.y = data[1]
      self.z = data[2]
    elif isinstance(data, dict):
      self.x = data['x']
      self.y = data['y']
      self.z = data['z']
    else:
      raise Exception

  def __repr__(self):
    return '<Vec3: {:.3f}, {:.3f}, {:.3f}>'.format(self.x, self.y, self.z)

  def __add__(v1, v2):
    if isinstance(v2, Vec3):
      return Vec3(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z)
    elif isinstance(v2, int) or isinstance(v2, float) or isinstance(v2, long):
      return Vec3(v1.x+v2, v1.y+v2, v1.z+v2)

  def __sub__(v1, v2):
    if isinstance(v2, Vec3):
      return Vec3(v1.x-v2.x, v1.y-v2.y, v1.z-v2.z)
    elif isinstance(v2, int) or isinstance(v2, float) or isinstance(v2, long):
      return Vec3(v1.x-v2, v1.y-v2, v1.z-v2)    

  def __div__(v1, v2):
    if isinstance(v2, Vec3):
      return Vec3(v1.x/v2.x, v1.y/v2.y, v1.z/v2.z)
    elif isinstance(v2, int) or isinstance(v2, float) or isinstance(v2, long):
      return Vec3(v1.x/v2, v1.y/v2, v1.z/v2)    
