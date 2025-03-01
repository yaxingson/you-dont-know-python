# Python Data Model

The data model specifies the interfaces for building modules in the Python language itself (such as sequences, iterators, functions, classes, and context managers).

By implementing special methods in custom objects, the following language constructs can be realized and supported:

- Iteration
- Collection classes
- Attribute access
- Operator overloading
- Function and method calls
- Object creation and destruction
- String representation and formatting
- Context management

Example:

```py
from collections import namedtuple
from random import choice, shuffle

Card = namedtuple('Card', ('rank', 'suit'))

class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

  def __getitem__(self, key):
    return self.cards[key]

  def __setitem__(self):
    pass

  def __iter__(self):
    pass

  def __len__(self):
    return len(self.cards)

deck = FrenchDeck()

print(len(deck))

print(deck[0], deck[-1])
print(choice(deck))
print(deck[12::13])

for card in reversed(deck):
  pass

print(Card('7', 'beasts') in deck)

def spades_high(card):
  suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
  rank_value = FrenchDeck.ranks.index(card.rank)
  return rank_value, suit_values[card.suit]

for card in sorted(deck, key=spades_high):
  print(card)

```

> [doctest](https://docs.python.org/3/library/doctest.html)

```py
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
    return Vector(self.x + other.x, self.y + other.y)
  
  def __mul__(self, scalar):
    return Vector(self.x * scalar, self.y * scalar)
  
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

```

> The interactive console and debugger use the `repr` function to obtain the string representation of an object, while the `print` function uses the `str` function to get the string representation of an object. When an object does not define a `__str__` method, the Python interpreter will call the object's `__repr__` method as a substitute.

By default, the boolean value of instances of custom classes is always true unless the class has its own implementation of the `__bool__` or `__len__` methods.
