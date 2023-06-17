import sqlite3
try:
    db=sqlite3.connect('Employee')
    mycursor=db.cursor()
    data=[(11111,'Nehal','IT',75000),(22222,'Swaraj','Management',85000),(33333,'Aishu','sales',50000)]
    mycursor.execute('''insert into emp values (44444,'swara','HR',65000)''')
    mycursor.executemany('''insert into emp values(?,?,?,?)''',data)

except Exception as E:
    print("unable to connect with database")
else:
    db.commit()
    print("data inserted succesfully")
finally:
    db.close()