import mysql.connector
from config3 import config as cfg


db = mysql.connector.connect(
host="localhost",
user="root",
password=cfg["password"],
database="datarepresentation"
)

cursor = db.cursor()
sql="select * from student where id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)

cursor.close()
db.close()