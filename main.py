from tkinter import *
from PIL import Image,ImageTk
import subprocess

root = Tk()
root.geometry("940x500")
root.maxsize(940,500)
root.config(bg="white")
def you():
    subprocess.call(["python","ytcon.py"])
def ig():
    subprocess.call(["python","igcon.py"])    
def fb():
    subprocess.call(["python","fb.py"])    
# Label_title=Label(root,text="CINETUNE",font="arial 30 bold",borderwidth=5,relief="solid",background="blue")      #solid dotted inset outset ridge flat sunken(border types)
# Label_title.pack(pady=20)

#buttoncolor
def on_enter(event):
    event.widget["background"]="white"
def on_leaveyt(event):
    event.widget["background"]="red"    
def on_leaveig(event):
    event.widget["background"]="purple"
def on_leavefb(event):
    event.widget["background"]="blue"            

# frm=Frame(root,width=900,height=400)
# frm.place(x=60,y=150)

#bgimage
image1=ImageTk.PhotoImage(Image.open("bg4.png"))
background_label = Label(root, image=image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# name=ImageTk.PhotoImage(Image.open("rth.png"))
# name_label=Label(image=name).pack(pady=10)
# # name_label.place(x=830,y=6)
# # name_label.pack()

# logo=ImageTk.PhotoImage(Image.open("jj.png"))
# logo_label=Label(image=logo)
# logo_label.place(x=830,y=6)

img = ImageTk.PhotoImage(Image.open(r"D:\projects\converter\logos\youtube.png"))
img_label=Label(image=img)
img_label.place(x=40,y=180)


# frm2=Frame(root,width=40,height=30)
# frm2.place(x=500,y=145)
# img2=ImageTk.PhotoImage(Image.open("instagram.png"))
# img2_label=Label(frm2,image=img2)
# img2_label.pack()

img2=ImageTk.PhotoImage(Image.open(r"D:\projects\converter\logos\instagram.png"))
img2_label=Label(image=img2)
img2_label.place(x=370,y=160)


img3=ImageTk.PhotoImage(Image.open(r"D:\projects\converter\logos\facebook.png"))
img3_label=Label(image=img3)
img3_label.place(x=680,y=160)


#buttons
you_con=Button(root,text="YOUTUBE CONVERTER", padx=10,pady=3,command=you,background="red",font="Times_New_Roman 15 bold")
you_con.place(x=15,y=390)
you_con.bind("<Enter>",on_enter)
you_con.bind("<Leave>",on_leaveyt)

ins_con=Button(root,text="INSTAGRAM CONVERTER",padx=10,pady=3,command=ig,background="purple",font="Times_New_Roman 15 bold")
ins_con.place(x=318,y=390)
ins_con.bind("<Enter>",on_enter)
ins_con.bind("<Leave>",on_leaveig)

fb_con=Button(root,text="FACEBOOK CONVERTER",padx=10,pady=3,command=fb,background="blue",font="Times_New_Roman 15 bold")
fb_con.place(x=640,y=390)
fb_con.bind("<Enter>",on_enter)
fb_con.bind("<Leave>",on_leavefb)

mainloop()