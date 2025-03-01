from math import hypot

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return 'Vector({!r}, {!r})'.format(self.x, self.y)

  def __str__(self):
    return 'Vector({!s}, {!s})'.format(self.x, self.y)

  def __abs__(self):
    return round(hypot(self.x, self.y), 2)
  
  def __bool__(self):
    return bool(self.x or self.y)
  
  def __add__(self, other):
    return Vector(self.x+other.x, self.y+other.y)
  
  def __mul__(self, scalar):
    return Vector(self.x*scalar, self.y*scalar)
  
  def __rmul__(self, other):
    pass

v1 = Vector(2, 4)
v2 = Vector(2, 1)

v3 = Vector('1', '2')

print(v1 + v2)
print(abs(v1))
print(v1 * 3)

print(v3)
print(repr(v3))

