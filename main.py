from cryptography.fernet import Fernet
from auth import signup
from util import connect, db_name


def setup():
    con = connect()
    cur = con.cursor()
    cur.execute(f"create database if not exists {db_name}")
    cur.execute(f"use {db_name}")
    cur.execute("create table if not exists doctors(doc_id int primary key, name varchar(25), dept varchar(25))")
    cur.execute("create table if not exists patients(id int primary key, name varchar(25), doc_id int, foreign key(doc_id) references doctors(doc_id))")
    cur.execute("create table if not exists pharmacy(id int primary key, med_name varchar(25), stock int, price int)")
    cur.execute("create table if not exists users(id int primary key, username varchar(25), password varchar(500))")
    cur.execute("create table if not exists misc(encrypt_key varchar(500))")
    key_fetch = "select * from misc"
    cur.execute(key_fetch)
    res = cur.fetchall()
    if len(res) == 0:
        key = Fernet.generate_key()
        cur.execute("insert into misc values('{}')".format(key.decode("utf-8")))
    cur.close()
    con.commit()
    con.close()


if __name__ == "__main__":
    setup()
    signup("hi", "hil", False)
