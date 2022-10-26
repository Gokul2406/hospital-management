from util import connect
from termcolor import colored

conn = connect()
cur = conn.cursor()

cur.execute("use sabarmathi_hospital")

def add_med():
    med_name = input("Enter medicine name: ")
    med_id = int(input("Enter medicine id: "))
    price_per_tab = int(input("Enter price: "))
    stock = int(input("Enter stock available: "))

    cur.execute("insert into pharmacy values({}, '{}', {}, {})".format(med_id, med_name, stock, price_per_tab))
    conn.commit()
    print(colored('Success', 'green', attrs=['bold']), end='\n\n')

def remove_med():
    med_id = int(input("Enter medicine id to remove: "))
    try:    
        cur.execute("delete from pharmacy where id = {}".format(med_id))
    except Exception as e:
        print(e)
    print(colored('Success', 'green', attrs=['bold']), end='\n\n')

def show_med():
    cur.execute("select * from pharmacy")
    res = cur.fetchall()

    for i in res:
        print("Id: ", i[0])
        print("Name: ", i[1])
        print("Stock left: ", i[2])
        print("Price: ", i[3])
        print("----------------------", end="\n\n")

def update_med():
    id = int(input("Enter medicine id: "))
    new_val = input("Enter new value: ")
    col = input("""Available columns
                   1) Id
                   2) Name (med_name)
                   3) Stock 
                   4) Price
    """)

    if col.lower() in ["id", "med_name", "stock", "price"]:
        cur.execute("update pharmacy set {} = '{}' where id = '{}'".format(col, new_val, id))
    else:
        print("Retry")
        update_med()
    print(colored('Success', 'green', attrs=['bold']), end='\n\n')