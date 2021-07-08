import tkinter, random,data
from tkinter import *

num=random.randrange(0,9,1)
cmt=0

def design(t):
    t.geometry('400x400')
    t.iconbitmap(r'a.ico')
    t.title('Jumble Craze')
 
def reset(l1,e1):
    global num ,cmt
    cmt.destroy()
    num=random.randrange(0,9,1)
    l1.configure(text=data.word[num])
    e1.delete(0,END)


    
	
def default(l1):
    global num
    l1.configure(text=data.word[num])
    
def checkans(e1,rt):
    global num, cmt
    var=e1.get()
    if var == data.answer[num]:
        cmt=Label(rt, text="Correct Answer", font=("Courier New",10,"bold"), bg="green",fg="white" )
        cmt.place(x=140,y=240)
    else:
        cmt=Label(rt, text=" Wrong Answer ", font=("Courier New",10,"bold"),bg="red", fg="#FFFFFF" )
        cmt.place(x=140,y=240)
        e1.delete(0,END)


def game(rt):
    global num, cmt
    wrd=Label(rt, text=data.word[num], font=("Comic sans ms",28,"bold"),relief= RIDGE,bd=15 ,fg="#000000" )
    wrd.pack(pady=40, ipady=10,ipadx=10)

    ans=StringVar()
    e=Entry(rt,font=("Comic sans ms",28),width=15,textvariable=ans,justify='center')
    e.place(x=29,y=177)
    msg=Label(rt, text="Type the words in small letters!", font=("Courier New",8,"bold"),bg="#cccccc",fg="#FFFFFF" )
    msg.place(x=86,y=150)
    check=Button(rt, text="Check",font=("Times New Roman",16,"bold"), width=10, bg='#4C4848', fg='#FFFFFF',command=lambda:checkans(e,rt))
    check.place(x=50,y=270)
    nxt=Button(rt, text="Next",font=("Times New Roman",16,"bold"), width=10, bg='#4C4848', fg='#FFFFFF',command=lambda:reset(wrd,e))
    nxt.place(x=220,y=270)



def start(t):
    play=Button(t, text="Play",font=("Comic sans ms",16,"bold"), width=25, bg='lightgrey', fg='#FFFFFF', relief= GROOVE,command=lambda:game(t))
    play.place(x=29,y=180)


