import os
from dotenv import load_dotenv
from pymysql import apilevel, threadsafety, paramstyle, connect
from pymysql import Warning, InterfaceError, DatabaseError, DataError, OperationalError
from pymysql import Binary, STRING, BINARY, NUMBER

load_dotenv()

partners = [
  {'name':'Nell Adkins', 'email':'pivehivav@nuzit.us'},
  {'name':'Phoebe Wagner', 'email':'vokas@labtirev.ml'},
  {'name':'Sylvia Long', 'email':'sipizde@luge.bq'},
  {'name':'Addie Griffith', 'email':'mav@tonioli.pa'},
  {'name':'Birdie Holmes', 'email':'kuum@coj.bq'},
]

conn = connect(
  database='test',
  user='root', 
  password=os.getenv('MYSQL_PASSWD')
)

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS partners(name VARCHAR(30), email TEXT)')
cur.executemany('INSERT INTO partners VALUES(%(name)s, %(email)s)', partners)
cur.execute('SELECT * FROM partners WHERE email LIKE "%.bq"')

for partner in cur.fetchall():
  print('<{!s}, {!s}>'.format(*partner))

cur.close()
conn.commit()
conn.close()

if __name__ == '__main__':
  print(apilevel, threadsafety, paramstyle)

