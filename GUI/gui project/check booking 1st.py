from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.geometry('1000x800')
Label(root,text=" ").grid(row=0,column=0)#.pack()

img=PhotoImage(file='python_bus.png')
Label(root,image=img).grid(row=0,column=2,columnspan=8)#.pack()

Label(root,text="Online Bus Booking System",font='arial 30 bold ',bg='bisque').grid(row=1,column=2,columnspan=8)#.pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").grid(row=2,column=0)#.pack()
Label(root,text=" ").grid(row=3,column=0)#.pack()
Label(root,text="Check Your Booking",bg='green',fg='white',padx=10).grid(row=4,column=2,columnspan=6)#.pack()
Label(root,text=" ").grid(row=5,column=0)#.pack()

Label(root,text='Enter Your Mobile No:').grid(row=7,column=2)
a=Entry(root)
a.grid(row=7,column=4)
Button(root,text='Check Booking').grid(row=7,column=6)

root.mainloop()
