import tkinter as tk
from tkinter import *
import pyttsx3


engine=pyttsx3.init()

def Speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

root=Tk()


def home_window():
    root.destroy()
    import mainhome

def translator_window():
    root.destroy()
    import translator

def music_window():
    root.destroy()
    import music

def CHATBOT_window():
    root.destroy()
    import chatbotpg


textv=StringVar()

obj=LabelFrame(root,text="Text to Speech",font=20,bd=1,bg="black",fg="white")
obj.pack(fill="both",expand="yes",padx=10)

lb1=Label(obj,text="Text",font=25,bg="black",fg="pink")
lb1.pack(side=tk.LEFT,padx=10,pady=10)

text=Entry(obj,textvariable=textv,font=30,width=55,bd=25)
text.pack(side=tk.LEFT,padx=10,pady=10)
#speak
btn=Button(obj,text="Speak",font=20,bg="black",fg="pink",cursor="hand2",command=Speaknow)
btn.pack(side=tk.LEFT,padx=10)

#translator
btn=Button(obj,text="TRANSLATOR",font=20,bg="black",fg="pink",cursor="hand2",command=translator_window)
btn.place(x=150,y=400)
#music player
btn=Button(obj,text="MUSIC",font=20,bg="black",fg="pink",cursor="hand2",command=music_window)
btn.place(x=300,y=400)
#chatbot
btn=Button(obj,text="HELP CHATBOT",font=20,bg="black",fg="pink",cursor="hand2",command=CHATBOT_window)
btn.place(x=400,y=400)

simpli_logo =PhotoImage(file="Audio.png")
Label(root,image=simpli_logo,bg="grey").place(x=10,y=50,height=200,width=700)

root.title("Langvertor - Text To Speech")
root.geometry("730x600")
root.resizable(False,False)
#icon
image_icon=PhotoImage(file="logo_project_sysbol.png")
root.iconphoto(False,image_icon)

root.mainloop()
