import customtkinter , tkinter
from tkinter import *

from playsound import playsound
from gtts import gTTS
import os , webbrowser , datetime , sqlite3 , googletrans , subprocess , pystray , threading , pyautogui , keyboard , time
import speech_recognition as sr
from PIL import Image
from pystray import MenuItem as item
from tkinter import messagebox
from selenium import webdriver
import random, pymem , requests as r , yt_dlp as youtube_dl


username = os.getlogin()
con = sqlite3.connect("lorai.db", check_same_thread=False) 
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS programsc (pn TEXT, pw TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS cmh (command TEXT, file TEXT)")

main = tkinter.Tk()
main.title("LorAI")
mainframe  = Frame()
mainframe.pack()
screen_width = int(int(main.winfo_screenwidth())/2)
screen_height = int(int(main.winfo_screenheight())/2)
main.geometry(f"{screen_width}x{screen_height}")
main.config(background="black")
main.resizable(width=False, height=False)

def show_page(page_name):
    for page in pages.values():
        page.pack_forget()
    pages[page_name].pack()

def add_button_to_label(label, text, command):
    button = Button(label, text=text, command=command)
    button.pack()


def optionmenu_callback(choice):
    if choice == "SC Manager":
        show_page("page1")



page1 = Frame(main)
label1 = Label(page1, text="Shortcut Manager",background="black",foreground="white",width=25,height=10)
label1.pack()
button = customtkinter.CTkButton(master=label1, text="add",fg_color="red",hover_color="gray", command="")
button.pack()
button0 = customtkinter.CTkButton(master=label1, text="remove",fg_color="red",hover_color="gray", command="")
button0.pack()

page2 = Frame(main)
label2 = Label(page2, text="Sayfa 2")
label2.pack()
add_button_to_label(label2, "Düğme 2", lambda: print("Button 2 clicked"))



page3 = Frame(main)
label3 = Label(page3, text="Sayfa 3")
label3.pack()

liste = cursor.execute("SELECT * FROM cmh")
data = liste.fetchall()

my_text_box=customtkinter.CTkTextbox(master=label3, height=5, width=40)
my_text_box.pack()

command=my_text_box.get("1.0","end-1c")

def add():
    with open(file=f"commands/{command}.py",mode="x",encoding="utf-8") as f:
            pass
    with open(file="loraicommands.py",mode="+a",encoding="utf-8") as f:
        f.writelines(f"\nfrom commands.{command} import *")
    cursor.execute("INSERT INTO cmh VALUES(?,?)",(command,f".command/{command}.py"))
    con.commit()
addb = customtkinter.CTkButton(master=label3, text="add",fg_color="red",hover_color="gray", command=add)
addb.pack()

def remove():
    cursor.execute("DELETE FROM cmh WHERE command = ?",[command])
    os.remove(path=f"commands/{command}.py")
    con.commit()
removeb = customtkinter.CTkButton(master=label3, text="remove",fg_color="red",hover_color="gray", command=remove)
removeb.pack()





page4 = Frame(main)
label4 = Label(page4, text="Sayfa 3")
label4.pack()
add_button_to_label(label4, "Düğme 3", lambda: print("Button 3 clicked"))

page5 = Frame(main)
label5 = Label(page5, text="Sayfa 3")
label5.pack()
add_button_to_label(label5, "Düğme 3", lambda: print("Button 3 clicked"))

page6 = Frame(main)
label6 = Label(page6, text="Sayfa 3")
label6.pack()
add_button_to_label(label6, "Düğme 3", lambda: print("Button 3 clicked"))

page7 = Frame(main)
label7 = Label(page7, text="Sayfa 3")
label7.pack()
add_button_to_label(label7, "Düğme 3", lambda: print("Button 3 clicked"))



pages = {
    "page1": page1,
    "page2": page2,
    "page3": page3,
    "page4": page4,
    "page5": page5,
    "page6": page6,
    "page7": page7
}


optionmenu = customtkinter.CTkOptionMenu(main,fg_color="red",button_color="red",button_hover_color="gray", values=["SC Manager","Password Manager","Credit Card Manager"],command=optionmenu_callback)
optionmenu.set("Managers")
optionmenu.place(relx=0.10, rely=0.1, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=main, text="Downloader",fg_color="red",hover_color="gray", command="")
button.place(relx=0.25, rely=0.1, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=main, text="Command Handler",fg_color="red",hover_color="gray", command=show_page("page3"))
button.place(relx=0.40, rely=0.1, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=main, text="Settings",fg_color="red",hover_color="gray", command="")
button.place(relx=0.55, rely=0.1, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=main, text="Computer",fg_color="red",hover_color="gray", command="")
button.place(relx=0.70, rely=0.1, anchor=customtkinter.CENTER)


main.mainloop()