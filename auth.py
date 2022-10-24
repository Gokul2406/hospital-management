from cryptography.fernet import Fernet
from random import randint
from util import connect, db_name

def signup(username, password, isAdmin):
    key_fetch = "select * from misc"
    con = connect()
    cur = con.cursor()
    cur.execute(f"use {db_name}")
    cur.execute(key_fetch)
    res = cur.fetchall()
    for keys in res:
        for key in keys:
            fernet = Fernet(key.encode())
            enc_pass = fernet.encrypt(password.encode())
            cur.execute("insert into users values({}, '{}', '{}')".format(1, username, enc_pass.decode("utf-8")))
            cur.close()
            con.commit()
            con.close()
            print("success")
            




