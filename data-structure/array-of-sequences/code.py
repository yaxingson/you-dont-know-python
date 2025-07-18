"""
>>> bytes('你好', encoding='utf-8')
b'\xe4\xbd\xa0\xe5\xa5\xbd'

>>> symbols = '&^#$*@['
>>> [ord(symbol) for symbol in symbols]
[38, 94, 35, 36, 42, 64, 91]

>>> x = 'ABC'
>>> [ord(x) for x in x]
[65, 66, 67]
>>> x
'ABC'

>>> array('I', (ord(symbol) for symbol in 'abc'))
array('I', [97, 98, 99])

>>> user = ('Glenn Cobb', 'mo@idbakub.jm')
>>> name, email = user
>>> email
'mo@idbakub.jm'

>>> stocks = [('google', 78.2), ('apple', 101.4), ('meta', 86.0)]
>>> for stock in sorted(stocks, key=lambda item: item[1]):
...   print('%s/%d'%stock)
google/78
meta/86
apple/101

>>> args = (20, 8)
>>> divmod(*args)
(2, 4)

>>> _, filename = path.split('/d/workspace/repository/github/you-dont-know-python/pyproject.toml')
>>> filename
'pyproject.toml'

>>> Card = namedtuple('Card', 'rank suit')
>>> card = Card('J', 'clubs')
>>> card[0]
'J'

>>> Card._fields
('rank', 'suit')
>>> Card._make(('5', 'hearts'))
Card(rank='5', suit='hearts')
>>> card._asdict()
{'rank': 'J', 'suit': 'clubs'}

>>> isinstance(card._asdict(), (OrderedDict,))
False

>>> tuple(reversed((78, 10, 43)))
(43, 10, 78)

>>> ... is Ellipsis 
True

>>> len(set([id(obj) for obj in [[]]*5]))
1

>>> t = (4, 2, [78, 10])
>>> try:
...   t[2] += [34, 50]
... except TypeError as e:
...  str(e)
"'tuple' object does not support item assignment"

>>> t[2] += [0] #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
TypeError: 'tuple' object does not support item assignment

>>> t
(4, 2, [78, 10, 34, 50, 0])

>>> dis('t[2] += [7]')



"""
from dis import dis
from collections.abc import Container, Iterable, Sized, Sequence, MutableSequence
from collections import deque, namedtuple, OrderedDict
from array import array
from os import path
from gettext import gettext

class Foo:
  """
  >>> foo = Foo()
  >>> foo[12::13]
  slice(12, None, 13)
  >>> foo[0, 10, 3]
  (0, 10, 3)
  >>> foo[0:3, 5:9:2]
  (slice(0, 3, None), slice(5, 9, 2))
  >>> foo[3:...]
  slice(3, Ellipsis, None)

  """
  def __getitem__(self, pos):
    return pos
  
  def __setitem__(self, pos, value):
    pass

class Vector:
  """
  >>> v = Vector(2, 7)
  >>> prev_id = id(v)
  >>> v += Vector(-1, 8)
  >>> v
  Vector(1, 15)
  >>> prev_id == id(v)
  True

  """
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return 'Vector({!r}, {!r})'.format(self.x, self.y)

  def __add__(self, other):
    if isinstance(other, Vector):
      return Vector(self.x + other.x, self.y + other.y)
    elif isinstance(other, (int, float)):
      return Vector(self.x + other, self.y + other)
    else:
      raise TypeError('')

  def __iadd__(self, other):
    if isinstance(other, Vector):
      self.x += other.x
      self.y += other.y
      return self
    elif isinstance(other, (int, float)):
      self.x += other
      self.y += other
      return self
    else:
      raise TypeError('')

if __name__ == '__main__':
  import doctest
  doctest.testmod()
