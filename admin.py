from util import connect, db_name

con = connect()
cur = con.cursor()
cur.execute(f"use {db_name}")

def add_doctors():
    name = input("Enter name: ")
    id = int(input("Enter doctor id: "))
    dept = input("Enter doctor's department: ")
    salary = int(input("Enter salary: "))
    working_hrs = int(input("Enter time of consultancy: "))
    fees = int(input("Enter fees: "))
    doc_insert = f"insert into doctors values({id}, '{name}', '{dept}', {salary}, {working_hrs}, {fees})"

    cur.execute(doc_insert)
    cur.close()
    con.commit()
    print("success")
    con.close()
    
def remove_doctors():
    id = int(input("Enter doctor's id"))
    remove_doc = f"delete from doctors where doc_id = {id}"
    cur.execute(remove_doc)
    cur.close()
    con.commit()
    print("success")
    con.close()

