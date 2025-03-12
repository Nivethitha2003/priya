import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

from tkinter import *
import cv2
import mysql.connector as mysql

from numpy import result_type
from signature import match

import matplotlib.pyplot as plt

    
import tk as tk
from PIL import Image, ImageTk
import tkinter as tk

class ViewData:
    def __init__(self):
        def main():
            s1 = "C:\\Users\\DELL\\Desktop\\nivipj\\Fake_Signature_verification\\Fake_Signature_verification\\main.py"
            messagebox.showinfo("Success", s1)

        def Viewdata():
            workingDir = "C:\\Users\\DELL\\Desktop\\nivipj\\Fake_Signature_verification\\Fake_Signature_verification\\main.py"
            PATH = os.path.sep.join([workingDir, "main"])
            main_dir = os.path.join("C:\\Users\\DELL\\Desktop\\nivipj\\Fake_Signature_verification\\Fake_Signature_verification\\amain.py")


# Mach Threshold
THRESHOLD = 85

def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)  # add this



def capture_image_from_cam_into_temp(sign=1):
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cv2.namedWindow("test")

    # img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            if not os.path.isdir('temp'):
                os.mkdir('temp', mode=0o777)  # make sure the directory exists
            # img_name = "./temp/opencv_frame_{}.png".format(img_counter)
            if(sign == 1):
                img_name = "./temp/test_img1.png"
            else:
                img_name = "./temp/test_img2.png"
            print('imwrite=', cv2.imwrite(filename=img_name, img=frame))
            print("{} written!".format(img_name))
            # img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    return True


def captureImage(ent, sign=1):
    if(sign == 1):
        filename = os.getcwd()+'\\temp\\test_img1.png'
    else:
        filename = os.getcwd()+'\\temp\\test_img2.png'
    # messagebox.showinfo(
    #     'SUCCESS!!!', 'Press Space Bar to click picture and ESC to exit')
    res = None
    res = messagebox.askquestion(
        'Click Picture', 'Press Space Bar to click picture and ESC to exit')
    if res == 'yes':
        capture_image_from_cam_into_temp(sign=sign)
        ent.delete(0, tk.END)
        ent.insert(tk.END, filename)
    return True


def checkSimilarity(window, path1, path2):
    result = match(path1=path1, path2=path2)
    if(result <= THRESHOLD):
        messagebox.showerror("Failure: Signatures Do Not Match",
                             "Signatures are "+str(result)+f" % similar!!")
        pass
    else:
        messagebox.showinfo("Success: Signatures Match",
                            "Signatures are "+str(result)+f" % similar!!")
    return True




winmain = Tk()
winmain.title("Fake Signature Verification")
winmain.maxsize(width=900, height=800)
winmain.minsize(width=900, height=800)
winmain.configure(bg='#99ddff')


image1 = Image.open("3.jpg")
img = image1.resize((900, 800))
test = ImageTk.PhotoImage(img)

label1 = tk.Label(winmain, image=test)
label1.image = test

# Position image
label1.place(x=1, y=1)

# image1 = Image.open("3.png")
test = ImageTk.PhotoImage(img)

label1 = tk.Label(winmain, image=test)
label1.image = test

Label(winmain, text='Fake Signature Verification', bg="#34bfbb", font='verdana 15 bold') \
               .place(x=220, y=70)


root = tk.Tk()
root.title("Signature Matching")
root .geometry("500x700")  # 300x200
uname_label = tk.Label(root, text="Compare Two Signatures:", font=10)
uname_label.place(x=90, y=50)

img1_message = tk.Label(winmain, text="Signature 1", font=10)
img1_message.place(x=50, y=190)

image1_path_entry = tk.Entry(winmain, font=10)
image1_path_entry.place(x=170, y=190)

img1_capture_button = tk.Button(
    winmain, text="Capture", font=10,bg="#99ddff", command=lambda: captureImage(ent=image1_path_entry, sign=1))
img1_capture_button.place(x=400, y=150)

img1_browse_button = tk.Button(
    winmain, text="Browse", font=10,bg="#99ddff", command=lambda: browsefunc(ent=image1_path_entry))
img1_browse_button.place(x=400, y=200)

image2_path_entry = tk.Entry(winmain, font=10)
image2_path_entry.place(x=170, y=290)

img2_message = tk.Label(winmain, text="Signature 2", font=10)
img2_message.place(x=50, y=290)

img2_capture_button = tk.Button(
    winmain, text="Capture", font=10,bg="#99ddff", command=lambda: captureImage(ent=image2_path_entry, sign=2))
img2_capture_button.place(x=400, y=280)

img2_browse_button = tk.Button(
    winmain, text="Browse", font=10,bg="#99ddff", command=lambda: browsefunc(ent=image2_path_entry))
img2_browse_button.place(x=400, y=340)

compare_button = tk.Button(
    winmain, text="Compare", font=10,bg="#34bfbb", command=lambda: checkSimilarity(window=root,
                                                                   path1=image1_path_entry.get(),
                                                                   path2=image2_path_entry.get(),))

compare_button.place(x=200, y=380)
root.mainloop()

