from tkinter import *

root=Tk()
root.geometry('800x650')

img=PhotoImage(file='python_bus.png')
Label(root,image=img).pack()
Label(root,text="Online Bus Booking System",font='arial 30 bold ',fg='red',bg='bisque').pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").pack()
Label(root,text=" ").pack()
Label(root,text=" ").pack()
Label(root,text=" ").pack()

Label(root,text="Name: Shashank Bairagi",font='arial 10 bold',fg='brown').pack()
Label(root,text="Er : 221B343",font='arial 10 bold',fg='brown').pack()
Label(root,text="Mobile : 7024427539",font='arial 10 bold',fg='brown').pack()

Label(root,text=" ").pack()
Label(root,text=" ").pack()
Label(root,text=" ").pack()
Label(root,text=" ").pack()
Label(root,text=" ").pack()
Label(root,text="Submitted to : Dr. Mahesh Kumar",font='arial 10 bold',fg='brown',bg='bisque').pack()
Label(root,text="Project Based Learning",font='arial 10 bold',fg='red').pack()
root.mainloop()
