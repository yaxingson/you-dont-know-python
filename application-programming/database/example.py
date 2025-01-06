import unittest
import sqlite3
import sqlobject
from pymysql import apilevel, threadsafety, paramstyle, connect, Warning, \
  InterfaceError, DatabaseError, OperationalError, Date, Timestamp, STRING
from json import load
from sqlalchemy import Column

class TestDatabase(unittest.TestCase):
  def test_db_api(self):
    self.assertEqual(apilevel, '2.0')
    self.assertEqual(threadsafety, 1)
    self.assertEqual(paramstyle, 'pyformat')

  def test_connect(self):
    fp = open('config.json')
    config = load(fp)

    db = config['database']

    with connect(user=db['user'], passwd=db['passwd'], host='localhost', port=3306, database='test') as conn:
      cur = conn.cursor()
      
      self.assertEqual(cur.arraysize, 1)

      select_sql = 'SELECT * FROM products;'
      update_sql = 'UPDATE products SET prod_name="5 ton anvil" WHERE prod_id=\'ANV01\''

      cur.execute(update_sql)
      cur.execute(select_sql)
      
      self.assertEqual(cur.fetchone()[2], '5 ton anvil')
      self.assertEqual(len(cur.fetchall()), 13)

      conn.commit()
      cur.close()
  
    fp.close()

  def test_sqlite(self):
    with sqlite3.connect('sqlite_test') as conn:
      cur = conn.cursor()

      create_sql = '''
      CREATE TABLE users (
        username VARCHAR(20),
        email VARCHAR(30)
      );
      '''

      insert_sql = 'INSERT INTO users (username, email) VALUES (?, ?);'
      select_sql = 'SELECT * from users;'
      drop_sql = 'DROP TABLE users;'

      cur.execute(create_sql)
      cur.execute(insert_sql, ('Kate Richardson', 'lectesezi@hat.gr'))
      cur.execute(insert_sql, ('Lucille Garcia', 'bewisohog@deljar.jm'))
      cur.execute(insert_sql, ('Clayton Burgess', 'huhpucwe@ufmeam.li'))

      cur.execute(select_sql)
      self.assertEqual(len(cur.fetchall()), 3)
    
      cur.execute(drop_sql)

      cur.close()
      conn.commit()

  def test_sqlalchemy(self):
    pass
  
  def test_sqlobject(self):
    pass

  