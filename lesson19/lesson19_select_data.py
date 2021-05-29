import sqlite3

# create context manager with generator
con = sqlite3.connect('test.db')

### move this part under context manager
cur = con.cursor()

data = cur.execute("SELECT * FROM stocks")

for record in data:
    print(record)
###

con.close()

