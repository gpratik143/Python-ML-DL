from tkinter import *
root=Tk()
root.geometry('800x800')
Label(root,text=" ").grid(row=0,column=0)#.pack()

img=PhotoImage(file='python_bus.png')
Label(root,image=img).grid(row=0,column=2,columnspan=6)#.pack()
Label(root,text="Online Bus Booking System",font='arial 30 bold ',bg='bisque').grid(row=1,column=2,columnspan=6)#.pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").grid(row=2,column=0)#.pack()
Label(root,text=" ").grid(row=3,column=0)#.pack()
Label(root,text=" ").grid(row=4,column=0)#.pack()

Button(root,text="Seat Booking",bg='green',font='arial 10 bold ').grid(row=5,column=2)#.pack()
Button(root,text="Check Booked Seat",bg='green',font='arial 10 bold ').grid(row=5,column=4)#.pack()
Button(root,text="Add Bus Details",bg='green',font='arial 10 bold ').grid(row=5,column=6)#.pack()
Label(root,text=" ").grid(row=6,column=6)#.pack()
Label(root,text="For Admin Only",fg='red',font='arial 8 ').grid(row=7,column=6)#.pack()
root.mainloop()
