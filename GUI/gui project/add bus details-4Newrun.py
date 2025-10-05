from tkinter import *
from tkinter.messagebox import *

import sqlite3
con=sqlite3.Connection('ByDB')
cur = con.cursor()
cur.execute('create table if not exists newrun(busid int, rundate date,stid int)')

root=Tk()
root.geometry('800x600')
Label(root,text=" ").grid(row=0,column=0)#.pack()

img=PhotoImage(file='python_bus.png')
Label(root,image=img).grid(row=0,column=2,columnspan=8)#.pack()

Label(root,text="Online Bus Booking System",font='arial 30 bold ',bg='bisque').grid(row=1,column=2,columnspan=8)#.pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").grid(row=2,column=0)#.pack()
Label(root,text=" ").grid(row=3,column=0)#.pack()
Label(root,text="Add Bus Running Details",bg='grey88',fg='green',padx=10).grid(row=4,column=2,columnspan=7)#.pack()
Label(root,text=" ").grid(row=5,column=0)#.pack()

Label(root,text='Bus ID').grid(row=13,column=2)
ns=Entry(root)
ns.grid(row=13,column=3)

Label(root,text='Running Date').grid(row=13,column=4)
mn=Entry(root)
mn.grid(row=13,column=5)

Label(root,text='Seat Available').grid(row=13,column=6)
st=Entry(root)
st.grid(row=13,column=7)

def enter_detail():
    busid=ns.get()    
    #b_type=clicked.get()
    rundate=mn.get()
    stid=st.get()
    #email=em.get()
    cur.execute("insert into newrun(busid,rundate,stid) values(?,?,?)",(busid,rundate,stid))
    print('Route Details Added Successfully')
    print(*cur.execute('select * from newrun'))
    showinfo("Route","Route Added Successfull")
    con.commit()

ed=Entry(root)
def delete():
    cur.execute('delete from newrun where busid =?',(ed.get(),))
    showinfo("delete","Record Deleted")
    print('Route Details Updated')
    print(*cur.execute('select * from newrun'))
    
    con.commit()

def edit():
    
    ed.grid(row=15,column=9,columnspan=10)
    Label(root,text='Enter BusID:').grid(row=15,column=8)
    Button(root,text='Delete',command=delete).grid(row=16,column=9,columnspan=10)
 

    
Button(root,text='Add Run',bg='light green',command=enter_detail,padx=7).grid(row=13,column=8)
Button(root,text='Delete Run',fg='red',bg='light green',command=edit).grid(row=13,column=9)

root.mainloop()
