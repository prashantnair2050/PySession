import sqlite3

#Connect to SQLite Database | Creating a new SQLite Database instance

conn = sqlite3.connect('test.db')
c = conn.cursor()

#Create table
c.execute('''
CREATE TABLE employee(eid int, ename text, esal int, dept text)
''')

c.execute('''
INSERT INTO employee values (1,"Prashant",10000,"Ops")
''')

#Commit
conn.commit()
conn.close()