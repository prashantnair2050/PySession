import sqlite3

#Connect to SQLite Database | Creating a new SQLite Database instance

conn = sqlite3.connect('test.db')
c = conn.cursor()

#Select --- Retrieval of data

c.execute('''
select * from employee;
''')


print(c.fetchall())

conn.close()