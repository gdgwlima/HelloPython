import sqlite3 as sql

database1 = sql.connect('test1.db')   #Si no existe la BD, Python la va a crear

db1Cursor = database1.cursor()   #Cursor para la base de datos creada

cmd = 'CREATE TABLE users(username TEXT, password TEXT)'
cmd2 = 'INSERT INTO users (username, password) VALUES ("testuser","testpassword")'
cmd3 = 'SELECT username, password FROM users'
db1Cursor.execute(cmd)     #Ejecutara la consulta en la base de datos
db1Cursor.execute(cmd2)
db1Cursor.execute(cmd3)
database1.commit()          #Sirve para guardar los cambios

for x in db1Cursor:
    print (x)


