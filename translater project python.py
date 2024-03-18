from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change (text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masseges = sor_txt.get(1.0,END)
    textget = change(text=masseges,src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)






root = Tk()
root.title("Translater")
root.geometry("500x700")
root.config(bg='Red')

Lab_txt = Label(root,text="Translater",font=("Time New Roman",40,"bold"))
Lab_txt.place(x=100,y=40,height=50,width=300)

Frame = Frame(root).pack(side=BOTTOM)

Lab_txt = Label(root,text="source Text",font=("Time New Roman",20,"bold"))
Lab_txt.place(x=100,y=100,height=20,width=300)

sor_txt = Text(Frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(Frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("English")

button_change = Button(Frame,text = "Treanslate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(Frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("English")

dest_txt = Text(Frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

Lab_txt = Label(root,text="Dest Text",font=("Time New Roman",20,"bold"))
Lab_txt.place(x=100,y=360,height=20,width=300)

root.mainloop()