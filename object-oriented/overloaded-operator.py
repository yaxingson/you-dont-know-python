"""
>>> ~2
-3

>>> ctx = getcontext()
>>> ctx.prec = 40

>>> val = Decimal('1') / Decimal('3')

>>> val
Decimal('0.3333333333333333333333333333333333333333')
>>> val == +val
True

>>> ctx.prec = DefaultContext.prec
>>> val == +val
False

>>> +val
Decimal('0.3333333333333333333333333333')

>>> ct = Counter('honorificabilitudinitatibus') 
>>> ct
Counter({'i': 7, 't': 3, 'o': 2, 'n': 2, 'a': 2, 'b': 2, 'u': 2, 'h': 1, 'r': 1, 'f': 1, 'c': 1, 'l': 1, 'd': 1, 's': 1})

>>> ct['i'] = 0
>>> ct['t'] = -3

>>> ct
Counter({'o': 2, 'n': 2, 'a': 2, 'b': 2, 'u': 2, 'h': 1, 'r': 1, 'f': 1, 'c': 1, 'l': 1, 'd': 1, 's': 1, 'i': 0, 't': -3})

>>> +ct
Counter({'o': 2, 'n': 2, 'a': 2, 'b': 2, 'u': 2, 'h': 1, 'r': 1, 'f': 1, 'c': 1, 'l': 1, 'd': 1, 's': 1})

"""
import math
from decimal import Decimal, getcontext, DefaultContext
from collections import Counter
from itertools import zip_longest

class Vector:
  """
  >>> v = Vector([3, 4])
  
  >>> abs(v)
  5.0
  >>> -v
  Vector(-3, -4)
  >>> +v
  Vector(3, 4)
  >>> ~v

  >>> v1 = Vector([3, 4, 5])
  >>> v2 = Vector([6, 7, 8])
  
  >>> v1 + v2
  Vector(9, 11, 13)

  >>> v1 + v2 == Vector([3+6, 4+7, 5+8])
  True
  
  >>> v1 + (10, 20)
  Vector(13, 24, 5)

  """
  
  def __init__(self, iterable):
    self.iterable = iterable
  
  def __iter__(self):
    return iter(self.iterable)

  def __repr__(self):
    return f'Vector({", ".join(str(x) for x in self)})'

  def __eq__(self, other):
    return any(x == y for x, y in zip(self, other))

  def __abs__(self):
    return math.sqrt(sum(x * x for x in self))
  
  def __neg__(self):
    return Vector(-x for x in self)

  def __pos__(self):
    return Vector(self)

  def __invert__(self):
    pass
  
  def __add__(self, other):
    pairs = zip_longest(self, other, fillvalue=0)
    return Vector(x + y for x, y in pairs)
