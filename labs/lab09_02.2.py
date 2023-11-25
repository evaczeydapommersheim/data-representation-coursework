import mysql.connector
from config3 import config as cfg

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=cfg["password"],
    database = "datarepresentation"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

mycursor.execute(sql)

mycursor.close()
connection.close()