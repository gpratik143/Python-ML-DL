from tkinter import *
root=Tk()
root.geometry('700x600')
Label(root,text=" ").grid(row=0,column=0)#.pack()

img=PhotoImage(file='python_bus.png')
Label(root,image=img).grid(row=0,column=2,columnspan=8)#.pack()
Label(root,text="Online Bus Booking System",font='arial 30 bold ',bg='bisque').grid(row=1,column=2,columnspan=8)#.pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").grid(row=2,column=0)#.pack()
Label(root,text=" ").grid(row=3,column=0)#.pack()
Label(root,text="Enter Journey Details",bg='green',fg='white',padx=10).grid(row=4,column=2,columnspan=6)#.pack()
Label(root,text=" ").grid(row=5,column=0)#.pack()
a=Entry(root)
a.grid(row=7,column=2)
b=Entry(root)
b.grid(row=7,column=4)#pack()
c=Entry(root)
c.grid(row=7,column=6)#pack()
Label(root,text="To:").grid(row=7,column=1)#.pack()
Label(root,text="From:").grid(row=7,column=3)#.pack()
Label(root,text="Journey Date:").grid(row=7,column=5)#.pack()

Button(root,text='Show Bus',bg='green').grid(row=7,column=7)
Button(root,text='Home',bg='green').grid(row=7,column=8)

Label(root,text=" ").grid(row=6,column=6)#.pack()
#Label(root,text="For Admin Only",font='arial 8 ').grid(row=7,column=6)#.pack()
root.mainloop()

