import unittest
import http
import ftplib
import urllib3
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlparse, urlunparse, urljoin, quote, unquote, \
  quote_plus, unquote_plus, urlencode

class TestWebClientServer(unittest.TestCase):
  def test_urlparse(self):
    url = 'https://docs.python.org/zh-cn/3.13/library/unittest.html'
    parse_result = urlparse(url)

    self.assertEqual(parse_result.netloc, 'docs.python.org')
    self.assertEqual(urlunparse(parse_result), url)

  def test_urljoin(self):
    base_url = 'http://www.python.org/doc/FAQ.html'
    new_url = 'http://www.python.org/doc/current/lib/lib.html'
    self.assertEqual(urljoin(base_url, 'current/lib/lib.html'), new_url)

  def test_urlopen(self):
    with urlopen('https://httpbin.org/') as res:
      self.assertEqual(res.geturl(), 'https://httpbin.org/')

  def test_urlretrieve(self):
    def report_hook(blocks, block_size, total_size):
      pass

    filename, response_headers = urlretrieve('https://httpbin.org/get', 
      filename='httpbin-get.json', reporthook=report_hook)

    self.assertEqual(filename, 'httpbin-get.json')
    self.assertEqual(response_headers.get('Content-Type'), 'application/json')

  def test_quote(self):
    base = 'http://www/~foo/cgi-bin/s.py?name=joe mama&num=6'

    self.assertEqual(quote(base), 'http%3A//www/~foo/cgi-bin/s.py%3Fname%3Djoe%20mama%26num%3D6')
    self.assertEqual(quote_plus(base), 'http%3A%2F%2Fwww%2F~foo%2Fcgi-bin%2Fs.py%3Fname%3Djoe+mama%26num%3D6')
  
  def test_urlencode(self):
    search_params = {'name': 'Georgina Garcia', 'email': 'jo@ifo.pr'}

    self.assertEqual(urlencode(search_params), 'name=Georgina+Garcia&email=jo%40ifo.pr')

