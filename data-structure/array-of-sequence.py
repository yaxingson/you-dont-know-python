"""
>>> bytearray('人生苦短,我用python', encoding='utf-8')
bytearray(b'\xe4\xba\xba\xe7\x94\x9f\xe8\x8b\xa6\xe7\x9f\xad,\xe6\x88\x91\xe7\x94\xa8python')

>>> type(b'xml')
<class 'bytes'>

>>> type('répertoire')
<class 'str'>

>>> codes = [36, 162, 163, 165, 8364, 164]
>>> ''.join(chr(code) for code in codes)
'$¢£¥€¤'

>>> {'id':'001', 'username':'', 'email':'', 
...   'address':{} }
{'id': '001', 'username': '', 'email': '', 'address': {}}

>>> x = 'ABC'
>>> [ord(x) for x in x]
[65, 66, 67]
>>> x
'ABC'

>>> symbols = '$¢£¥€¤'
>>> [ord(s) for s in symbols if ord(s) > 8000]
[8364]

>>> array('I', (ord(symbol) for symbol in symbols))
array('I', [36, 162, 163, 165, 8364, 164])

>>> city, year, *rest = ('Tokyo', 2003, 32450, 0.66, 8014)
>>> year
2003
>>> rest
[32450, 0.66, 8014]

>>> traveler_ids = [('USA', '1672615'), ('BRA', '6716219'), ('ESP', 'CE891S0')]
>>> for passport in sorted(traveler_ids):
...   print('%s/%s'%passport)
BRA/6716219
ESP/CE891S0
USA/1672615

>>> a, b = 78, 56
>>> a, b = b, a
>>> a, b
(56, 78)

>>> t = (20, 8)
>>> quotient, _ = divmod(*t)
>>> quotient
2

>>> _, filename = path.split('/home/workspace/playground/package.json')
>>> filename
'package.json'

>>> City = namedtuple('City', 'name country population coordinates')
>>> tokyo = City('Tokyo', 'JP', 36.977, (35.68, 139.69))
>>> tokyo[0], tokyo.country
('Tokyo', 'JP')

>>> City._fields
('name', 'country', 'population', 'coordinates')

>>> delhi_data = ('Delhi NCR', 'IN', 21.93, (28.61, 77.20))
>>> delhi = City._make(delhi_data)
>>> delhi
City(name='Delhi NCR', country='IN', population=21.93, coordinates=(28.61, 77.2))

>>> delhi._asdict()
{'name': 'Delhi NCR', 'country': 'IN', 'population': 21.93, 'coordinates': (28.61, 77.2)}

"""
import gettext
from os import path
from collections import deque
from array import array
from collections.abc import MutableSequence, Sequence, Container, Iterable, Sized
from collections import namedtuple, OrderedDict
