import sqlite3

# create context manager with class
con = sqlite3.connect('test.db')

### move this part under context manager
cur = con.cursor()

cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

con.commit()
###

con.close()


