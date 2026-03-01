r"""
>>> html = '''
... <p>
...  <b>hello,world!</b>
... </p>
... '''.strip()
>>> html
'<p>\n <b>hello,world!</b>\n</p>'
>>> is_match('.+', html, DOTALL)
True
>>> is_match(r'\A<\w+>', html)
True
>>> search(r'</\w+>\Z', html).group()
'</p>'

>>> match(r'^\d+\.\d{1,3}\$$', '9.920$').group()
'9.920$'
>>> is_match('[^aeiou]', 'y')
True
>>> is_match('</?[^>]+>', '<root>')
True

>>> match_obj = match(r'(\d{4})/(\d{2})/(\d{2})', '2026/02/02')
>>> match_obj.group()
'2026/02/02'
>>> match_obj.group(1)
'2026'
>>> match_obj.groups()
('2026', '02', '02')

>>> is_match('.end', 'end')
False

>>> match(r'\w+@((\w+\.)*)\w+\.com', 'nobody@www.xxx.yyy.zzz.com').group(1)
'www.xxx.yyy.'

>>> sub(r'(\d{2}|\d{4})/(\d{2})/(\d{2})', r'\1-\2-\3', '2026/02/02')
'2026-02-02'

>>> split(r', |(?= (?:\d{5}|[A-Z]{2})) ', 'Mountain View, CA 94040')
['Mountain View', 'CA', '94040']

>>> findall(r'(?i)yes', 'yes? Yes. YES!!')
['yes', 'Yes', 'YES']


"""
import os
from re import (search, match, compile, purge, findall, finditer, 
                sub, subn, split, DOTALL)

def is_match(pattern, string, flags=0):
  return match(pattern, string, flags) is not None


with open('ll_data.txt', encoding='utf8') as f:
  for line in f:
    print(split(r'\s{1,}', line.strip(), maxsplit=8))

with os.popen('tasklist') as f:
  for line in f:
    print(line)
