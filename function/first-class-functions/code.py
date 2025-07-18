"""
>>> def factorial(n):
...   '''return n!'''
...   return 1 if n < 2 else n * factorial(n - 1)

>>> factorial(42)
1405006117752879898543142606244511569936384000000000

>>> factorial.__doc__
'return n!'

>>> type(factorial)
<class 'function'>

>>> help(factorial)
Help on function factorial in module __main__:
<BLANKLINE>
factorial(n)
    return n!
<BLANKLINE>

>>> reduce(add, range(101))
5050

>>> all([]), any([])
(True, False)

>>> [callable(o) for o in (abs, str, 13)]
[True, True, False]

"""
from functools import reduce
from operator import add

if __name__ == '__main__':
  import doctest
  doctest.testmod()
