# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:31:54 2022

@author: Ace
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("mini note pad")
root.geometry("600x400")
root.minsize(650,650)
root.maxsize(700,700)
root.configure(background="lightblue")

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.03,anchor=CENTER)

my_text= Text(root,height=35,width=80,background="gray")
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

def open_file():
    print("hi")

open_button=Button(root,image=open_img,text="OpenFile",command=open_file)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
root.mainloop()