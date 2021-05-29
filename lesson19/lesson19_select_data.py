import sqlite3


con = sqlite3.connect('test.db')

cur = con.cursor()

data = cur.execute("SELECT * FROM stocks")

for record in data:
    print(record)

con.close()

