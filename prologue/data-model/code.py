"""
>>> card = Card('7', 'diamonds')
>>> card.rank
'7'

"""
from collections import namedtuple
from random import choice, shuffle
from math import hypot

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  """
  >>> deck = FrenchDeck()
  >>> card = choice(deck)
  >>> card.rank in FrenchDeck.ranks
  True
  >>> card.suit in FrenchDeck.suits
  True

  >>> len(deck[12::13])
  4

  >>> for card in reversed(deck): # doctest: +ELLIPSIS
  ...   print(card)
  Card(rank='A', suit='hearts')
  Card(rank='K', suit='hearts')
  Card(rank='Q', suit='hearts')
  ...

  >>> Card('j', 'hearts') in deck
  False

  >>> shuffle(deck)
  >>> len(deck)
  52

  """
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits 
      for rank in self.ranks]

  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, pos):
    return self._cards[pos]
  
  def __setitem__(self, pos, item):
    self._cards[pos] = item

class Vector:
  """
  >>> v = Vector()
  >>> v
  Vector(0, 0)

  >>> print(v)
  [0, 0]

  >>> v + Vector(2, 7)
  Vector(2, 7)
  >>> v
  Vector(0, 0)

  >>> 3 * Vector(2, 7)
  Vector(6, 21)
  
  """
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def __repr__(self):
    return 'Vector({!r}, {!r})'.format(self.x, self.y)
  
  def __str__(self):
    return '[{!s}, {!s}]'.format(self.x, self.y)

  def __abs__(self):
    return hypot(self.x, self.y)
  
  def __bool__(self):
    return bool(self.x or self.y)

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __mul__(self, scalar):
    return Vector(self.x * scalar, self.y * scalar)
  
  def __rmul__(self, scalar):
    return self * scalar

class Foo:
  """
  >>> foo = Foo()
  >>> bool(foo)
  False
  """
  def __len__(self):
    return 0

if __name__ == '__main__':
  import doctest
  doctest.testmod()
