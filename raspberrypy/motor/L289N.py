from ..utils.GPIO_utils import setup_output, output, GPIO_Base
from time import sleep
import random

def keep_decorate(func):
  def func_wrapper(self, keep=None):
    func(self, keep)
    if keep is None: keep = self.keep
    if keep > 0:
      sleep(keep)
      self.stop()
  return func_wrapper

class L289N(GPIO_Base):
  def __init__(self, pins=(40,38,  37,35,), keep=1.0, **kwargs):
    '''
      mode: the pin mode, 'BOARD' or 'BCM'.
      pins: pins for left forward, left backward, right forward, right backward.
      keep: the duration an action is kept, if keep <= 0 then the motor will not stop
    '''
    super(L289N, self).__init__(**kwargs)

    self.pins = pins
    for pin in pins: setup_output(pin)

    self.keep = keep

  # ============== actions ================
  def stop(self):
    output(self.pins, [0,0,0,0])

  @keep_decorate
  def left_backward(self, keep=None):
    output(self.pins[:2], [0, 1])
  @keep_decorate
  def left_forward(self, keep=None):
    output(self.pins[:2], [1, 0])
  @keep_decorate
  def right_backward(self, keep=None):
    output(self.pins[-2:], [0, 1])
  @keep_decorate
  def right_forward(self, keep=None):
    output(self.pins[-2:], [1, 0])
  @keep_decorate
  def forward(self, keep=None):
    self.right_forward(keep=-1)
    self.left_forward(keep=-1)
  @keep_decorate
  def backward(self, keep=None):
    self.right_backward(keep=-1)
    self.left_backward(keep=-1)
  @keep_decorate
  def spin_right(self, keep=None):
    self.right_backward(keep=-1)
    self.left_forward(keep=-1)
  @keep_decorate
  def spin_left(self, keep=None):
    self.right_forward(keep=-1)
    self.left_backward(keep=-1)
