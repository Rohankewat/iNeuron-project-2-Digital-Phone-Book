import psycopg2
from datetime import datetime

dt = datetime.today()
d = dt.strftime("%d-%m-%Y and %I:%M:%S")
print(d)

connection = psycopg2.connect(user = "postgres",
                             password = "rohankewat",
                             port = "5432",
                             database = "postgres",
                             host = "localhost")
connection.autocommit = True
Cursor = connection.cursor()
Cursor.execute("create table registration (user_id int,user_name text,user_password text,primary key(user_id))")
print("please do registration first")
user_id = input("Enter user id ")
user_name = input("Enter username ")
user_password = input("Enter user password ")
try:
    Cursor.execute("insert into registration values (%s,%s,%s)",(user_id,user_name,user_password,))
    print("you are registered succesfully")
    print("you can login now")  
    def funct_name():
        l1 = []
        l2 = []
        a = input("Enter user name ")
        b = input("Enter user password ")
        Cursor.execute("select user_name from registration where user_id = %s",(user_id,))
        result_1 = Cursor.fetchone()
        Cursor.execute("select user_password from registration where user_id = %s",(user_id,))
        result_2 = Cursor.fetchone()
        l1.append(a)
        l2.append(b)
        n1 = tuple(l1)
        n2 = tuple(l2)
        if n1 == result_1 and n2 == result_2:
            print("you are logged in sucesfully")
        else:
            print("may be you enter either wrong  user_password or wrong user_name")
            funct_name()
    funct_name()
except Exception:
    print("you are already registered")
    print("please login")
    def log_funct():
        l1 = []
        l2 = []
        a = input("Enter user name ")
        b = input("Enter user password ")
        Cursor.execute("select user_name from registration where user_id = %s",(user_id,))
        result_1 = Cursor.fetchone()
        Cursor.execute("select user_password from registration where user_id = %s",(user_id,))
        result_2 = Cursor.fetchone()
        l1.append(a)
        l2.append(b)
        n1 = tuple(l1)
        n2 = tuple(l2)  
        if n1 == result_1 and n2 == result_2:
            print("you are logged in sucesfully")
        else:
           print("may be you enter either wrong user_password or wrong user_name")
           log_funct()
    log_funct()
finally:
    Cursor.execute("create table dig_phonebook (id int, name text, contact int,email text,primary key(id))")
    print("Enter 1 -> for add contact")    
    print("Enter 2 -> for read all contact")
    print("Enter 3 -> for delete contact")
    print("Enter 4 -> for update contact")    
    print("Enter 5 -> for read specific conact no")  
    print("Enter 6 -> for delete all contacts")
k = int(input("Select above option "))
if k == 1:
    try:   
        c = input("Enter id ")
        d = input("Enter name ")
        e = input("Enter contact no ")
        f = input("Enter email ") 
        Cursor.execute("insert into dig_phonebook values (%s,%s,%s,%s)",(c,d,e,f,))
        print("contact added sucessfully")
    except:
        print("your contacts already added")
elif k == 2:
    try:
        Cursor.execute("select * from dig_phonebook")
        result = Cursor.fetchall()
        for e in result:
            print(e)
    except:
        print("you dont have added contacts yet")
elif k==3:
    try:
        delete = input("Enter id")
        Cursor.execute("delete from dig_phonebook where id = %s",(delete,))
        print("contact deleted sucessfully")
    except:
        pass
elif k==4:
    try:
        update = input("Enter new contact no ")
        id = input("Enter id ")
        Cursor.execute("update dig_phonebook set contact = %s where id = %s ",(update,id,))
        print("contact no updated sucessfully")
    except:
        pass 
elif k==5:
    try:
        name = input("Enter name ")
        Cursor.execute("select contact from dig_phonebook where name = %s",(name,))
        new_result = Cursor.fetchall()
        print(new_result)
    except:
        pass
elif k == 6:
    try:
        Cursor.execute("DROP TABLE dig_phonebook")
        print("All contacts deleted sucessfully")
    except Exception:
        print("you already deleted contacts")
Cursor.close()