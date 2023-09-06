from tkinter import* 
import tkinter as tk 
from tkinter import ttk, filedialog

root=Tk()
root.title("Langvertor - Home")
root.geometry("883x495")
root.resizable(False,False)

def audio_window():
    root.destroy()
    import audio

def music_window():
    root.destroy()
    import music

def chat_window():
    root.destroy()
    import chatbotpg

def translator_window():
    root.destroy()
    import translator

Mainbg=PhotoImage(file="mainbg.png")
Label(root,image=Mainbg,bg="#0f1a2b").place(x=0,y=0)

translate=Button(root,text="Translator",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=15,height=1,bg="Red",fg="Black",command= translator_window)
translate.place(x=405,y=212)

translate=Button(root,text="Text to Speech",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=15,height=1,bg="Red",fg="Black",command= audio_window)
translate.place(x=647,y=210)

translate=Button(root,text="Music Player",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=15,height=1,bg="Red",fg="Black",command= music_window)
translate.place(x=405,y=324)

translate=Button(root,text="Help ChatBot",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=15,height=1,bg="Red",fg="Black",command= chat_window)
translate.place(x=647,y=324)

#icon
image_icon=PhotoImage(file="logo_project_sysbol.png")
root.iconphoto(False,image_icon)

root.mainloop()
