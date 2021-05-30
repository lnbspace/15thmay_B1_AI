import sqlite3
db = sqlite3.connect('mydb.sqlite')

db.execute('create table if not exists calc_history (id int, expression text, result float)')
db.commit()
db.close()
