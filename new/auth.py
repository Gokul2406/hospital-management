from cryptography.fernet import Fernet
import random
from util import connect, db_name

def signup(username, password):
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
            id = random.randint(1, 100)
            cur.execute("insert into users values({}, '{}', '{}')".format(id, username, enc_pass.decode("utf-8")))
            cur.close()
            con.commit()
            con.close()
            print("success")
            
def login(user, password):
    key_fetch = "select * from misc"
    con = connect()
    cur = con.cursor()
    cur.execute(f"use {db_name}")
    cur.execute(key_fetch)
    res = cur.fetchall()
    login_res = False
    for keys in res:
        for key in keys:
            fernet = Fernet(key.encode())
            cur.execute(f"select password from users where username = '{user}'")
            user = cur.fetchall()
            for values in user:
                for enc_password in values:
                    dec_pass = fernet.decrypt(enc_password.encode()).decode()
                    if dec_pass == password:
                        print("login success")
                        login_res = True
                        
                    else:
                        print("no")
    return login_res


