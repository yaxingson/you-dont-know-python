"""
>>> def factorial(n):
...  '''return n!'''
...  return 1 if n < 2 else n * factorial(n-1)
...

>>> factorial(42)
1405006117752879898543142606244511569936384000000000

>>> factorial.__doc__
'return n!'

>>> type(factorial)
<class 'function'>

>>> help(factorial)
Help on function factorial in module first-class-function:
<BLANKLINE>
factorial(n)
    return n!
<BLANKLINE>

>>> fact = factorial
>>> id(fact) == id(factorial)
True

>>> list(map(factorial, range(5)))
[1, 1, 2, 6, 24]

>>> list(filter(lambda n: n % 2, range(6)))
[1, 3, 5]

>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=len)
['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']

>>> reduce(add, range(101))
5050

>>> sum(range(101))
5050

>>> all([]), any([])
(True, False)

>>> [callable(o) for o in (strftime, BingoCage.pick, BingoCage, BingoCage([]))]
[True, True, True, True]

>>> upper_case_name.__dict__
{'short_description': 'Customer name'}

>>> print(tag('p', 'hello', 'world', cls="sidebar", id=3))
<p class="sidebar" id="3">hello</p>
<p class="sidebar" id="3">world</p>

>>> tag(alt='placeholder', name='img')
'<img alt="placeholder" />'

>>> kwargs = {'name':'img', 'src':'sunset.jpg', 'cls':'framed'}
>>> tag(**kwargs)
'<img class="framed" src="sunset.jpg" />'

"""
from functools import reduce
from operator import add
from time import strftime
from random import shuffle

def upper_case_name(obj):
  return '{0.first_name} {0.last_name}'.format(obj).upper()

upper_case_name.short_description = 'Customer name'


def tag(name, *content, cls=None, **attrs):
  if cls is not None:
    attrs['class'] = cls
  
  if attrs:
    attr_str = ''.join(f' {attr}="{val}"' for attr, val in sorted(attrs.items()))
  else:
    attr_str = ''

  if content:
    return '\n'.join(f'<{name}{attr_str}>{c}</{name}>' for c in content)
  else:
    return f'<{name}{attr_str} />'

class BingoCage:
  def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

  def __init__(self, items):
    self._items = list(items)
    shuffle(self._items)

  def pick(self):
    try:
      return self._items.pop()
    except IndexError:
      raise LookupError('pick from empty BingoCage!')

  def __call__(self):
    return self.pick()
