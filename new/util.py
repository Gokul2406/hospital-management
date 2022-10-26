import mysql.connector as m

def connect():
    con = m.connect(host="localhost", user="root", password="root")
    return con

db_name = "sabarmathi_hospital"
