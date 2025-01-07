import unittest
from re import match, search, compile, DOTALL

class TestRegexp(unittest.TestCase):
  def test_special_symbol(self):
    self.assertRegex('bet', 'bat|bet|bit')
    self.assertRegex('.#\n', compile(r'\...', flags=DOTALL))
    self.assertRegex('From Submit', '^From')
    self.assertRegex('/d/bin/ls.sh', r'/bin/ls\.sh$')
    self.assertRegex('Subject:hi', '^Subject:hi$')
    self.assertRegex('r3po', '[cr][23][dp][o2]')
    self.assertRegex(' ', '[^aeiou]')
    self.assertRegex(' ', '[^\t\n]')
    self.assertRegex('6299278172612', '[0-9]{5,}')
    self.assertRegex('</a>', '</?[^>]+>')
    self.assertRegex('a_', '[A-Za-z]\w*')

  def test_match(self):
    pass

  def test_search(self):
    pass


