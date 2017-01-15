import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "gp")
cursor = db.cursor()

query = 'SELECT * FROM SCHEDULE'
cursor.execute(query)

data = cursor.fetchone()
print data
db.close()