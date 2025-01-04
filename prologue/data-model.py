"""
>>> version = sys.version_info
>>> '{0.major}.{0.minor}.{0.micro}'.format(version)
'3.8.2'

>>> version, *_ = sys.version.split(' ')
>>> version
'3.8.2'

>>> card = Card('7', 'diamonds')
>>> card[0]
'7'
>>> card.suit
'diamonds'

"""
import sys
from math import hypot
from collections import namedtuple
from random import choice, shuffle


Card = namedtuple('Card', ['rank', 'suit'])

def spades_high(card: Card):
  suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
  rank_value = FrenchDeck.ranks.index(card.rank)
  return rank_value * len(suit_values) + suit_values[card.suit]

class FrenchDeck:
  """
  >>> FrenchDeck.suits
  ['spades', 'diamonds', 'clubs', 'hearts']
  
  >>> deck = FrenchDeck()
  
  >>> len(deck)
  52
  
  >>> deck[-1]
  Card(rank='A', suit='hearts')
  
  >>> card = choice(deck)
  >>> card in deck
  True
  
  >>> deck[12::13]
  [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
  
  >>> for card in reversed(deck): # doctest: +ELLIPSIS
  ...  print(card)
  Card(rank='A', suit='hearts')
  ...

  >>> for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
  ...  print(card)
  Card(rank='2', suit='clubs')
  Card(rank='2', suit='diamonds')
  Card(rank='2', suit='hearts')
  ...

  """
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, pos):
    return self._cards[pos]
  
  def __contains__(self, item):
    return item in self._cards
  
  def __iter__(self):
    return iter(self._cards)

class Vector:
  """
  >>> v1 = Vector(3, 4)
  >>> v2 = Vector(2, 1)
  
  >>> v1 + v2
  Vector(5, 5)

  >>> abs(v1)
  5.0

  >>> v1 * 3 
  Vector(9, 12)
  
  """

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)

  def __repr__(self):
    return f'Vector({self.x}, {self.y})'
  
  def __abs__(self):
    return hypot(self.x, self.y)
  
  def __mul__(self, scalar):
    return Vector(self.x * scalar, self.y * scalar)

