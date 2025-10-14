"""
>>> provider, model = ('openai', 'gpt-3.5-turbo') 
>>> provider
'openai'

>>> bot = ChatBot()
>>> bot.model
'gpt-5'
>>> bot.model = 'gemini-2.5-pro'
Traceback (most recent call last):
AttributeError: attribute "model" is read only

>>> color_theme = ColorTheme('dark', 'night owl')
>>> color_theme.name
'night owl'

>>> editor = Editor()
>>> len(editor)
6
>>> isinstance(choice(editor), ColorTheme)
True
>>> for color_theme in reversed(editor): # doctest: +ELLIPSIS
...   print(color_theme)
ColorTheme(theme='dark', name='visual studio')
ColorTheme(theme='dark', name='winter is coming')
...
>>> ColorTheme(theme='light', name='visual studio') in editor
True
>>> for color_theme in sorted(editor): # doctest: +ELLIPSIS
...   print(color_theme)
ColorTheme(theme='dark', name='night owl')
...
>>> shuffle(editor) # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
TypeError: 'Editor' object does not support item assignment

>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v3 = Vector(0, 0)
>>> v1 + v2
Vector(4, 5)
>>> v1 * 3
Vector(6, 12)
>>> 2 * v2
Vector(4, 2)
>>> abs(Vector(3, 4))
5.0
>>> bool(v3)
False
>>> v3
Vector(0, 0)
>>> print(v3)
[0, 0]


"""
from collections import namedtuple
from random import choice, shuffle
from math import hypot

class ReadOnly:
  def __init__(self, attr_name, init_value):
    self.attr_name = attr_name
    self.value = init_value
  
  def __get__(self, instance, cls):
    return self.value
  
  def __set__(self, instance, value):
    raise AttributeError(f'attribute "{self.attr_name}" is read only')

  def __del__(self, instance):
    pass

class ChatBot:
  model = ReadOnly('model', 'gpt-5')

ColorTheme = namedtuple('ColorTheme', ['theme', 'name'])

class Editor:
  themes = ['light', 'dark']
  names = ['night owl', 'winter is coming', 'visual studio']

  def __init__(self):
    self._color_themes = [ColorTheme(theme, name) for theme in self.themes 
      for name in self.names]
  
  def __len__(self):
    return len(self._color_themes)
  
  def __getitem__(self, pos):
    return self._color_themes[pos]


class Vector:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return 'Vector({!r}, {!r})'.format(self.x, self.y)
  
  def __str__(self):
    return '[{!s}, {!s}]'.format(self.x, self.y)

  def __bool__(self):
    return bool(self.x or self.y)

  def __abs__(self):
    return hypot(self.x, self.y)

  def __add__(self, other):
    return Vector(self.x+other.x, self.y+other.y)
  
  def __mul__(self, scalar):
    return Vector(self.x*scalar, self.y*scalar)
  
  def __rmul__(self, scalar):
    return self * scalar
  




