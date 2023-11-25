import mysql.connector
from config3 import config as cfg


db = mysql.connector.connect(
host="localhost",
user="root",
password=cfg["password"],
database="datarepresentation"
)

cursor = db.cursor()
sql="delete from student where id = %s"
values = (1,)

cursor.execute(sql, values)
db.commit()
print("delete done")

cursor.close()
db.close()