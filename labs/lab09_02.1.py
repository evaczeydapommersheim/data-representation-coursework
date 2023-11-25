import mysql.connector
from config3 import config as cfg

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=cfg["password"]
)

mycursor = connection.cursor()

mycursor.execute("CREATE database datarepresentation")
mycursor.close()
connection.close()
