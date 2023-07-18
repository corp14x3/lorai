import sqlite3
con = sqlite3.connect("lorai.db", check_same_thread=False)
liste = con.execute("SELECT * FROM  drpc")
data = liste.fetchall()
print(data)