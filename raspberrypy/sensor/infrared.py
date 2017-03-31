from ..utils.GPIO_utils import setup_input, fetch, GPIO_Base

class InfraRed(GPIO_Base):
  '''
    unknown type
  '''
  def __init__(self, pin=12, **kwargs):
    super(InfraRed, self).__init__(**kwargs)
    self.pin = pin
    setup_input(pin)
  
  def get_blocked(self):
    return fetch(self.pin)==0
    
    
