import tkinter as tk
def OnButtonClick():
    welcome_label.config(text="Welcome..")
root=tk.Tk()
root.title("button example")
button=tk.Button(root,text='go',command=OnButtonClick)
button.pack(pady=50)
welcome_label=tk.Label(root,text='')
welcome_label.pack()
root.mainloop()
    