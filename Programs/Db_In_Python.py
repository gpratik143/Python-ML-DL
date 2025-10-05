from tkinter import * 
import sqlite3
con=sqlite3.Connection('MyDB.db')
cur=con.cursor()
cur.execute('create table if not exists emp(id number,name varchar(20))')

root=Tk()
Label(root,text="Database Demo",font="Arial 20").grid(row=0,column=1)
Label(root,text="Enter Id").grid(row=1,column=0)
er1=Entry(root)
er1.grid(row=1,column=1)
Label(root,text="Enter name").grid(row=1,column=2)
er2=Entry(root)
er2.grid(row=1,column=3)
def fun():
    Label(root,text="Demo..").grid(row=2,column=1)
    cur.execute('insert into emp values(?,?)',(int(er1.get()),er2.get()))
    con.commit()
    cur.execute('select * from emp')
    Label(root,text=cur.fetchall()).grid(row=3,column=0,columnspan=5)
Button(root,text="save",command=fun).grid(row=2,column=2)
root.mainloop()
