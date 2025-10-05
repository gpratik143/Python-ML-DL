from tkinter import*
root=Tk()
root.title("Image In GUI")
moon=PhotoImage(file="Moon.jpg")
Label(root,image=moon).grid(row=0,column=1)
root.mainloop()
