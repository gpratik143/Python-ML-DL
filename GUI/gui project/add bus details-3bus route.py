from tkinter import *
from tkinter.messagebox import *


import sqlite3
con=sqlite3.Connection('ByDB')
cur = con.cursor()
cur.execute('create table if not exists route(routeid int, stname varchar(30),stid int)')

root=Tk()
root.geometry('800x600')
Label(root,text=" ").grid(row=0,column=0)#.pack()

img=PhotoImage(file='python_bus.png')
Label(root,image=img).grid(row=0,column=2,columnspan=8)#.pack()

Label(root,text="Online Bus Booking System",font='arial 30 bold ',bg='bisque').grid(row=1,column=2,columnspan=8)#.pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").grid(row=2,column=0)#.pack()
Label(root,text=" ").grid(row=3,column=0)#.pack()
Label(root,text="Add Bus Route Details",bg='grey88',fg='green',padx=10).grid(row=4,column=2,columnspan=7)#.pack()
Label(root,text=" ").grid(row=5,column=0)#.pack()


Label(root,text='Route ID').grid(row=13,column=2)
ns=Entry(root)
ns.grid(row=13,column=3)

Label(root,text='Station Name').grid(row=13,column=4)
mn=Entry(root)
mn.grid(row=13,column=5)

Label(root,text='Station Id').grid(row=13,column=6)
si=Entry(root)
si.grid(row=13,column=7)


def enter_detail():
    routeid=ns.get()
    #b_type=clicked.get()
    stname=mn.get()
    stid=si.get()
    #email=em.get()
    cur.execute("insert into route(routeid,stname,stid) values(?,?,?)",(routeid,stname,stid))
    print('Route Details Added Successfully')
    print(*cur.execute('select * from route'))
    showinfo("Route","Route Added Successfull")
    con.commit()

ed=Entry(root)
def delete():
    cur.execute('delete from route where routeid =?',(ed.get(),))
    showinfo("delete","Record Deleted")
    print(*cur.execute('select * from route'))
    
    con.commit()

def edit():
    
    ed.grid(row=15,column=9,columnspan=10)
    Label(root,text='Enter RouteID:').grid(row=15,column=8)
    Button(root,text='Delete',command=delete).grid(row=16,column=9,columnspan=10)
 

Button(root,text='Add Route',bg='light green',command=enter_detail,padx=10).grid(row=13,column=8)

Button(root,text='Delete Route',fg='red',bg='light green',command=edit,padx=10).grid(row=13,column=9)

con.commit()
print(cur.fetchall())
root.mainloop()
