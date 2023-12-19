import customtkinter , tkinter
from tkinter import *


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

page2 = Frame(main)
label2 = Label(page2, text="Sayfa 2")
label2.pack()
add_button_to_label(label2, "Düğme 2", lambda: print("Button 2 clicked"))

page3 = Frame(main)
label3 = Label(page3, text="Sayfa 3")
label3.pack()
add_button_to_label(label3, "Düğme 3", lambda: print("Button 3 clicked"))

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
button = customtkinter.CTkButton(master=main, text="Command Handler",fg_color="red",hover_color="gray", command="")
button.place(relx=0.40, rely=0.1, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=main, text="Settings",fg_color="red",hover_color="gray", command="")
button.place(relx=0.55, rely=0.1, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=main, text="Computer",fg_color="red",hover_color="gray", command="")
button.place(relx=0.70, rely=0.1, anchor=customtkinter.CENTER)


main.mainloop()