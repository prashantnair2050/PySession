import sqlite3

#Connect to SQLite Database | Creating a new SQLite Database instance

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute('''select * from employee where dept="Dev"''')

print("Employees from Dev Dept")
print(c.fetchall())


c.execute('''select eid,ename from employee where dept="Dev"''')

print("Employee Names from Dev Dept")
print(c.fetchall())


c.execute('''select eid,ename from employee where dept="Dev" and esal > 500000''')

print("Employee Names from Dev Dept")
print(c.fetchall())
conn.close()