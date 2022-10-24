import mysql.connector as m

def connect():
    db_name = "hospital"
    con = m.connect(host="localhost", user="root", password="root")
    return con

db_name = "hospital"
