#1)
from tkinter import *
root=Tk()
hwl=Label(root,text="Hello World!!")
hwl.pack()
exitB=Button(root,text="Exit",width=55,command=root.destroy,)
exitB.pack(side=BOTTOM)
root.mainloop()

#2)
from tkinter import *
def write():
    p=Label(text="file")
    p.pack()
    p.mainloop()
root=Tk()
frame=Frame(root)
frame.pack()
l=Label(frame,text="Hello World!!")
l.pack()
b1=Button(frame,text="INFORMATION",width=50,command=write)
b1.pack(side=LEFT)
exitB=Button(root,text="Exit",width=50,command=root.destroy,)
exitB.pack(side=BOTTOM)
root.mainloop()

#3)
from tkinter import *
root=Tk()
text=0
def text_change():
    global text
    text += 1
    if text > 4:
        text = 1
    print("changed to:", text)
    b1.config(text=text)
def text_print():
    print("current:", text)

hwL=Label(root,text="Hello World!!")
hwL.pack()
b1=Button(text="CURRENT INFORMATION",width=25,command=text_print)
b1.pack()
b2 = Button(text="INFORMATION CHANGED", width=25, command=text_change)
b2.pack()
exitB=Button(text="Exit",width=25,command=root.destroy,)
exitB.pack(side=BOTTOM)
root.mainloop()

#4)
from tkinter import *
root = Tk()
root.geometry('300x300')
L1 = Label(text='NAME',background='yellow')
L1.pack()
e1 = Entry(L1)
e1.pack()
def write() :
    ent = e1.get()
    L2= Label(root,text ='Your name is :  \n %s'%(ent),background='pink')
    L2.pack()
b= Button (root, text = "SUBMIT", command = write)
b.pack()
button_1 = Button (root, text = "Exit", command = root.destroy)
button_1.pack(side=BOTTOM)
root.mainloop()

