import mysql.connector
from config3 import config as cfg


db = mysql.connector.connect(
host="localhost",
user="root",
password=cfg["password"],
database="datarepresentation"
)

cursor = db.cursor()
sql="update student set name = %s, age = %s where id = %s"
values = ("Joe",33, 1)

cursor.execute(sql, values)
db.commit()
print("update done")

cursor.close()
db.close()