from cryptography.fernet import Fernet
from auth import signup, login
from pharmacy import add_med, remove_med, show_med, update_med
from util import connect
from admin import add_doctors, remove_doctors, add_patients, remove_patients, update_doctors, update_patients, view_doctors, view_patients
import sys
from termcolor import colored, cprint

con = connect()
cur = con.cursor()


def setup():

    db_name = "sabarmathi_hospital"
    cur.execute(f"create database if not exists {db_name}")
    cur.execute(f"use {db_name}")
    cur.execute("create table if not exists doctors(doc_id int primary key, name varchar(25), dept varchar(25), salary varchar(10), fees varchar(10))")
    cur.execute("create table if not exists patients(id int primary key, name varchar(25), age varchar(5), doc_id varchar(5), reason varchar(50))")
    cur.execute("create table if not exists pharmacy(id int primary key, med_name varchar(25), stock varchar(5), price varchar(5))")
    cur.execute("create table if not exists users(id int primary key, username varchar(25), password varchar(500))")
    cur.execute("create table if not exists misc(encrypt_key varchar(500))")

    key_fetch = "select * from misc"
    cur.execute(key_fetch)
    res = cur.fetchall()
    if len(res) == 0:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        cur.execute("insert into misc values('{}')".format(key.decode()))
        cur.execute("insert into users values (1, 'admin', '{}')".format(fernet.encrypt('admin'.encode()).decode()))
    

    con.commit()



if __name__ == "__main__":
    setup()
    print('=====================', end="\n\n")
    print(colored('SABARMATHI HOSPITAL', 'red', attrs=['bold']), end="\n\n")
    print("""1) Login
2) Exit
    """)
    print('=====================', end="\n\n")

    
   
    while True:
        ch= int(input("Enter choice: "))
        if ch==1:
            username=input("ENTER USERNAME :")
            passwrd=input("ENTER PASSWRD :")
            res = login(username,passwrd)

            if res == True:
                while True:
                    print(colored('ADMIN MENU', 'red', attrs=['bold']), end="\n\n")   
                    print("""

                            1) Add doctors
                            2) Remove doctors
                            3) Update Doctors
                            4) View doctors
                            5) Add patient
                            6) Remove patients
                            7) Update patients
                            8) View patients

                            ****PHARMACY***
                            9) Add medicine
                            10) Remove medicine
                            11) View medicines
                            12) Update medicines
""")
                    ch = int(input("Enter choice: "))
                    if ch == 1:
                        add_doctors()
                    elif ch == 2:
                        remove_doctors()
                    elif ch == 3:
                        update_doctors()
                    elif ch == 4:
                        view_doctors()
                    elif ch == 5:
                       add_patients()
                    elif ch == 6:
                        remove_patients()
                    elif ch == 7:
                        update_patients()
                    elif ch == 8:
                        view_patients()
                    elif ch == 9:
                        add_med()
                    elif ch == 10:
                        remove_med()
                    elif ch == 11:
                        show_med()
                    elif ch ==12:
                        update_med()
            else:
                sys.exit(0)
                
        else:
            break

