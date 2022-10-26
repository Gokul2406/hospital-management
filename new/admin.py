
from util import connect, db_name
from termcolor import colored

con = connect()
cur = con.cursor()
cur.execute(f"use {db_name}")

def add_doctors():
    name = input("Enter name: ")
    id = int(input("Enter doctor id: "))
    dept = input("Enter doctor's department: ")
    salary = int(input("Enter salary: "))
    fees = int(input("Enter fees: "))
    doc_insert = f"insert into doctors values({id}, '{name}', '{dept}', {salary}, {fees})"
    cur.execute(doc_insert)

    con.commit()
    print(colored('Success', 'green', attrs=['bold']))


def update_doctors():
    print("""COLUMNS
            Name
            Department
            Salary
            Fees
        """)
    column = input("Enter column to update : ")
    if column.lower() in ["name", "department", "salary", "fees"]:
        new_val = input("Enter new value : ")
        id = int(input("Enter doctor's id : "))
        cur.execute("update doctors set {} = '{}' where doc_id = {}".format(column, new_val, id))
        print("Successfully updated")
    else:
        print("Please select from existing column")
        update_doctors()
   

    con.commit()
    print(colored('Success', 'green', attrs=['bold']), end='\n\n')
    
def remove_doctors():
    id = int(input("Enter doctor's id"))
    remove_doc = f"delete from doctors where doc_id = {id}"
    cur.execute(remove_doc)
    con.commit()
    print(colored('Success', 'green', attrs=['bold']), end='\n\n')


def view_doctors():
    cur.execute("select * from doctors")
    res = cur.fetchall()

    for i in res:
        print("___________________", end="\n\n")
        print("Doctor Id:- {}".format(i[0]))
        print("Doctor Name:- {}".format(i[1]))
        print("Doctor Department:- {}".format(i[2]))
        print("Doctor Salary:- {}".format(i[3]))
        print("Doctor Fees:- {}".format(i[4]))
        print("___________________", end="\n\n")

            

def add_patients():
    name = input("Enter name: ")
    age = int(input("Enter patients age: "))
    reason= input("Enter reason for consultancy: ")
    doc_id = int(input("Enter doctor id: "))
    id = int(input("Enter id"))
    pat_insert = f"insert into patients values({id}, '{name}', {age}, {doc_id}, '{reason}')"

    cur.execute(pat_insert)

    con.commit()
    print(colored('Success', 'green', attrs=['bold']), end='\n\n')



def remove_patients():
    id = input("Enter patient id: ")
    remove_pat = f"delete from patients where id = '{id}'"
    cur.execute(remove_pat)

    con.commit()
    print(colored('Success', 'green', attrs=['bold']), end='\n\n')


def update_patients():
    print("""COLUMNS
            Name
            Age
            Reason
            Doctor's Id (doc_id)
        """)
    column = input("Enter column to update : ")
    if column.lower() in ["name", "age", "reason", "doc_id"]:
        new_val = input("Enter new value : ")
        id = int(input("Enter patient's id : "))
        cur.execute("update patients set {} = '{}' where id = {}".format(column, new_val, id))
    
    else:
        print("Please select from existing column")
        update_doctors()
    con.commit()

    print(colored('Success', 'green', attrs=['bold']), end='\n\n')


def view_patients():
    cur.execute("select * from patients")
    res = cur.fetchall()

    for i in res:
        print("__________________", end="\n\n")
        print("Patient Id:- {}".format(i[0]))
        print("Patient Name:- {}".format(i[1]))
        print("Patient Age:- {}".format(i[2]))
        print("Doctor Assigned:- {}".format(i[3]))
        print("Patient's Reason:- {}".format(i[4]))
        print("___________________", end="\n\n")
