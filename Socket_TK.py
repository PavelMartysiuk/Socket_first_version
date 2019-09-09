from tkinter import *
from tkinter import messagebox
from client import get_massage

''' ПРиложение'''


def show_info():
    m = message.get()
    messagebox.showinfo('Books', get_massage(m))




root = Tk()
root.title("Find book")
root.geometry("500x500")

btn = Button(root, text="show", background='red', command=show_info)
btn.place(relx=.5, rely=.4, anchor="c")
message = StringVar()
message_entry = Entry(textvariable=message, width=20)
message_entry.place(relx=.5, rely=.1, anchor="c")
root.mainloop()
