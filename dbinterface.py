import sqlite3  #STEP 1
try:
    db=sqlite3.connect('Employee')   #STEP 2
    mycursor=db.cursor()   #STEP 3
    mycursor.execute('''create table if not exists emp
    (EmpID int NOT NULL,
    empName text,
    dept text,
    sal int,
    PRIMARY KEY(EmpID))''')   #STEP 4
except Exception as E:
    print("Unable to interact with db",E)
else:
    print("table created successfully")
finally:
    db.close()   #STEP 6
