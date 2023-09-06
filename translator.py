from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
from PIL import ImageTk, Image

root=Tk()
root.title("Langvertor - Translator")
root.geometry("1080x450")
root.resizable(True,True)
root.configure(bg="#0f1a2b")

def home_window():
    root.destroy()
    import mainhome

def audio_window():
    root.destroy()
    import audio

def music_window():
    root.destroy()
    import music

def chatbot_window():
    root.destroy()
    import chatbotpg


def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)
#icon
image_icon=PhotoImage(file="logo_project_sysbol.png")
root.iconphoto(False,image_icon)

Mainbg=PhotoImage(file="page_2.png")
Label(root,image=Mainbg,bg="#0f1a2b").place(x=0,y=0)

arrowbg=PhotoImage(file="arrow_.png")
Label(root,image=arrowbg,bg="#0f1a2b").place(x=475,y=70)

language=googletrans.LANGUAGES
languageV=list (language.values())
lang1=language.keys()

#1st combobox

combo1=ttk.Combobox (root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110,y=70)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold", bg="Black",fg="White", width=18, bd=5, relief=GROOVE,)
label1.place(x=10,y=100)

#2nd box
combo2=ttk.Combobox (root, values=languageV, font="Roboto 14", state="r",)
combo2.place(x=730,y=70)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="Black",fg="White", width=18, bd=5, relief=GROOVE)
label2.place(x=620,y=100)

#1st frame
f1=Frame(root,bg="White",bd=5)
f1.place(x=10,y=160,width=440,height=210)

text1=Text(f1,font="Robote 20",bg="Black",fg="White",relief=GROOVE,wrap=WORD,insertbackground='Red')
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f1)
scrollbar1.pack(side="right",fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#2st frame
f2=Frame(root,bg="White",bd=5)
f2.place(x=620,y=160,width=440,height=210)

text2=Text(f2,font="Robote 20",bg="Black",fg="White",relief=GROOVE,wrap=WORD,insertbackground='Red')
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f2)
scrollbar2.pack(side="right",fill='y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translation

translate=Button(root,text="Translate",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=10,height=2,bg="red",fg="white",command=translate_now)
translate.place(x=480,y=332)

Home=Button(root,text="Home",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=13,height=1,bg="blue",fg="white",command=home_window)
Home.place(x=128,y=403)

Music=Button(root,text="Music",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=13,height=1,bg="blue",fg="white",command= music_window)
Music.place(x=613,y=403)

speech=Button(root,text="Text to Speech",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=13,height=1,bg="blue",fg="white",command= audio_window)
speech.place(x=377,y=403)

chatbot=Button(root,text="Help Chatbot",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=13,height=1,bg="blue",fg="white",command= chatbot_window)
chatbot.place(x=841,y=403)

label_change()

root.mainloop()