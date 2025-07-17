# 文本处理

> 纯文本和XML-RPC服务

```py
#!/usr/bin/env python
import csv
from time import ctime
from urllib.request import urlopen 
from distutils.log import warn

data = [
  (9, 'Web Client and Server', 'base64,urllib'),
  (10, 'Web Programming: CGI & WSGI', 'cgi,time,wsgiref'),
  (13, 'Web Services', 'urllib,twython'),
]

with open('./external/book-data.csv', 'w', newline='\n') as f:
  writer = csv.writer(f)
  for record in data:
    writer.writerow(record)

with open('./external/book-data.csv') as f:
  reader = csv.reader(f)
  for chap, title, pkgs in reader:
    print(f'Chapter {chap}: {repr(title)} (featuring {pkgs})')

with open('./external/book-data.csv') as f:
  reader = csv.DictReader(f, fieldnames=('Chapter', 'Title', 'Packages'))
  for row in reader:
    print('Chapter {}: {!r} (featuring {})'.format(
      row['Chapter'], row['Title'], row['Packages']))

file_path = 'file:///D:\workspace\\repository\github\you-dont-know-python\\\
application-programming\\text-processing\external\\book-data.csv'

with urlopen(file_path) as opener:
  for row in opener:
    pass

```

<https://www.json.org/json-zh.html>

