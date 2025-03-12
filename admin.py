import os
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import messagebox, filedialog
import cv2
import mysql.connector as mysql
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
from cvlib.object_detection import draw_bbox
from main import ViewData

global act1

def act():
    x = Admin.get()
    y = password.get()
    if x == "nivi" and y == "nivi":
        s1 = "login successfully"
        messagebox.showinfo("success", s1)
        winadmin.destroy()  # Correct reference to the window object
        land = ViewData()  # Call to ViewData class (this should be implemented in main.py)
    else:
        messagebox.showinfo("login failed")

winadmin = Tk()
winadmin.title("ADMIN PAGE")
winadmin.maxsize(width=800, height=900)
winadmin.minsize(width=800, height=900)
winadmin.configure(bg='#34bfbb')

# Ensure this image exists in the directory where the script is run
try:
    image1 = Image.open("1.jpg")
    img = image1.resize((1100, 1000))
    test = ImageTk.PhotoImage(img)
    label1 = tk.Label(winadmin, image=test)
    label1.image = test
    label1.place(x=1, y=1)
except FileNotFoundError:
    print("Image '1.jpg' not found!")

Label(winadmin, text='Fake Signature Verification', bg="#ffb366", font='verdana 15 bold') \
    .place(x=250, y=150)

Admin = Label(winadmin, text="Admin", bg="#34bfbb", width=10, font='Verdana 10 bold')
Admin.place(x=210, y=320)

password = Label(winadmin, text="password", bg="#34bfbb", width=10, font='Verdana 10 bold')
password.place(x=210, y=370)

# Entry Box ------------------------------------------------------------------

Admin = StringVar()
password = StringVar()

Admin = Entry(winadmin, width=30, bg="silver", show='*', textvariable=Admin)
Admin.place(x=400, y=370)

password = Entry(winadmin, width=30, bg="silver", textvariable=password)
password.place(x=400, y=320)

Button(winadmin, text="login", font='Verdana 10 bold', bg="#34bfbb", command=act).place(x=340, y=520)

winadmin.mainloop()
