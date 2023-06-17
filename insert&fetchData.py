import sqlite3
try:
    db=sqlite3.connect('Employee')
    #db.text_factory
    cursor=db.cursor()
    cursor.execute('select * from emp')
    #print(cursor.fetchall())
    #print(cursor.fetchone())
    print(cursor.fetchmany(2))

    for each in cursor:
        print(each)
except Exception as E:
    print("unable to connect with database")
else:
    db.close()
    print("data succesfully fetched")