from tkinter import* 
import tkinter as tk 


root=Tk()
root.title("Langvertor - Help Chatbot")
root.geometry("883x495")
root.resizable(False,False)

def audio_window():
    root.destroy()
    import audio

def music_window():
    root.destroy()
    import music

def translator_window():
    root.destroy()
    import translator

Mainbg=PhotoImage(file="lastpage_bg.png")
Label(root,image=Mainbg,bg="#0f1a2b").place(x=0,y=0)

translate=Button(root,text="Yes?",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=10,height=1,bg='#9D9BFF',fg="Black",command= translator_window)
translate.place(x=401,y=172)

translate=Button(root,text="Yes?",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=10,height=1,bg='#9D9BFF',fg="Black",command= audio_window)
translate.place(x=401,y=270)

translate=Button(root,text="Yes?",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=10,height=1,bg='#9D9BFF',fg="Black",command= music_window)
translate.place(x=401,y=360)

#icon
image_icon=PhotoImage(file="logo_project_sysbol.png")
root.iconphoto(False,image_icon)

root.mainloop()