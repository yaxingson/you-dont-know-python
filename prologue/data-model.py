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
