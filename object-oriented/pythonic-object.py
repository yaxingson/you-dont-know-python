"""


"""
import math
from copy import copy
from array import array

class Vector:
  """
  >>> v = Vector(3, 4)
  >>> print(v.x, v.y)
  3.0 4.0

  >>> x, y = v
  >>> x, y
  (3.0, 4.0)

  >>> v
  Vector(3.0, 4.0)

  >>> v_clone = eval(repr(v))
  >>> v == v_clone
  True
  
  >>> print(v)
  (3.0, 4.0)

  >>> bytes(v)
  b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
  
  >>> abs(v)
  5.0

  >>> bool(v), bool(Vector(0, 0))
  (True, False)

  """
  typecode = 'd'
  
  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)

  @classmethod
  def create(cls):
    pass
  
  def __abs__(self):
    return math.hypot(self.x, self.y)
  
  def __bool__(self):
    return bool(abs(self))
  
  def __iter__(self):
    return (i for i in (self.x, self.y))

  def __hash__(self):
    pass
  
  def __repr__(self):
    cls_name = type(self).__name__
    return '{}({!r}, {!r})'.format(cls_name, *self)

  def __str__(self):
    return str(tuple(self))
  
  def __bytes__(self):
    return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

  def __format__(self, format_spec):
    pass
  
  def __eq__(self, other):
    return tuple(self) == tuple(other)
