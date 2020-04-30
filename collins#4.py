import tkinter as tk
import json
from difflib import get_close_matches
from tkinter import messagebox
data = json.load(open("data.json"))
screen=tk.Tk()
screen.title("Dict 4.0")
#screen.configure(background="crimson")
screen.geometry('500x500')
tk.Label(text="COLLINS", bg = "crimson",fg="black" ,font =("Segoe UI",15,'bold'),height=2).pack()
tk.Label(text="").pack()
tk.Label(text="").pack()
word = tk.StringVar()
ent=tk.Entry(bd=3 ,font =("Segoe UI",12), highlightcolor="light blue" ,width=35,textvariable=word).pack()
tk.Label(text="").pack()
t = tk.Message(bg="pink", text="")
def translate(w):
    str1 = w
    str2 = str1.lower()
    if str2 in json.load(open("data.json")):
        file1 = open("Dict4.0.txt", "r")
        file1.seek(0)
        all=file1.read()
        file1.close()
        file1 = open("Dict4.0.txt", "w")
        file1.write(str2+"\n")
        file1.close()
        file1 = open("Dict4.0.txt", "a")
        file1.write(all+"\n")
        file1.close()
        output = data[str2]
        t.configure(fg="black", bd=1, font=("Segoe UI", 13), width=600,  text=output,cursor="dot",relief="raised")
        t.pack()

    elif len(get_close_matches(str2, data.keys())) > 0:
        rly=tk.messagebox.askyesno("Dict 4.0", "Did you mean %s instead? " % get_close_matches(str2, data.keys())[0])

        if rly is True :
            file1 = open("Dict4.0.txt", "r")
            file1.seek(0)
            all = file1.read()
            file1.close()
            file1 = open("Dict4.0.txt", "w")
            file1.write(get_close_matches(str2, data.keys())[0]+"\n")
            file1.close()
            file1 = open("Dict4.0.txt", "a")
            file1.write(all+"\n")
            file1.close()
            output1 = data[get_close_matches(str2, data.keys())[0]]
            t.configure(fg="black", bd=1, font=("Segoe UI", 13),width=600,  text=output1,cursor="dot",relief="raised")
            t.pack()
        else :
            tk.messagebox.showinfo("Dict 4.0","Sorry the word does not exist")
    else:
        tk.messagebox.showinfo("Dict 4.0", "Please check the word you have entered")

def hist():
    file1=open("Dict4.0.txt", "r")
    file1.seek(0)
    l=[]
    hst=""
    for x in range(0,5,1) :
        l.append(file1.readline())
    for x in range(0,5,1):
        hst=hst+"\n"+l[x]
    t.configure(fg="black", bd=1, font=("Segoe UI", 13), width=600, text=hst, cursor="dot", relief="raised")
    t.pack()
    file1.close()
tk.Button(text="SEARCH", font=("Segoe UI", 12), command=lambda :translate(word.get())).pack()
tk.Label(text="").pack()
tk.Button(text="HISTORY", font=("Segoe UI", 12), command=hist).pack()
tk.Label(text="").pack()
screen.mainloop()








