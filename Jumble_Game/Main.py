import front_end, data, back_end, tkinter, random
from tkinter import *
from tkinter import messagebox

def main():
    back_end.greeting()
    root=tkinter.Tk()
    front_end.design(root)
    filename=PhotoImage(file=r"bg.png")
    bgl=Label(root,image=filename)
    bgl.place(x=0,y=0,relwidth=1,relheight=1)
    front_end.start(root)
    root.mainloop()


if __name__=="__main__":
    main()
