from os import path
from sqlite3 import apilevel, threadsafety, paramstyle, connect
from sqlite3 import Warning, InterfaceError, DatabaseError, DataError, OperationalError
from sqlite3 import Date, Time, Timestamp, DateFromTicks, TimeFromTicks

base_dir = path.dirname(path.abspath(__file__))

conn = connect(database=path.join(base_dir, 'partners.db'))

cur = conn.cursor()

partners = [
  ('Anthony Watson', 'suinipi@zauvikaf.gh'),
  ('Etta Perez', 'hi@daihoke.sv'),
  ('Verna Schwartz', 'az@fente.mo'),
  ('Dennis Abbott', 'ovjo@cibugrup.so'),
  ('Sylvia McBride', 'lacodco@bosef.as'),
]

cur.execute('CREATE TABLE IF NOT EXISTS partners(name VARCHAR(30), email TEXT)')
cur.executemany('INSERT INTO partners VALUES(?, ?)', partners)
cur.execute('SELECT * FROM partners')

for partner in cur.fetchall():
  print('<{!s}, {!s}>'.format(*partner))

cur.close()
conn.commit()
conn.close()


if __name__ == '__main__':
  print(apilevel, threadsafety, paramstyle)
