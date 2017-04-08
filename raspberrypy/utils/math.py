class Vec3(object):
  def __init__(self, data):
    if isinstance(data, list):
      self.x = data[0]
      self.y = data[1]
      self.z = data[2]
    elif isinstance(data, dict):
      self.x = data['x']
      self.y = data['y']
      self.z = data['z']

  def __repr__(self):
    return '<Vec3: {:.3f}, {:.3f}, {:.3f}>'.format(self.x, self.y, self.z)
