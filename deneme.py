import tkinter as tk

def show_page(page_name):
    for page in pages.values():
        page.pack_forget()
    
    pages[page_name].pack()

def add_button_to_label(label, text, command):
    button = tk.Button(label, text=text, command=command)
    button.pack()

root = tk.Tk()
root.geometry("400x300")

page1 = tk.Frame(root)
page2 = tk.Frame(root)
page3 = tk.Frame(root)

label1 = tk.Label(page1, text="Sayfa 1")
label1.pack()
add_button_to_label(label1, "Düğme 1", lambda: print("Button 1 clicked"))
label2 = tk.Label(page2, text="Sayfa 2")
label2.pack()
add_button_to_label(label2, "Düğme 2", lambda: print("Button 2 clicked"))
label3 = tk.Label(page3, text="Sayfa 3")
label3.pack()
add_button_to_label(label3, "Düğme 3", lambda: print("Button 3 clicked"))

pages = {
    "page1": page1,
    "page2": page2,
    "page3": page3
}

show_page("page1")

button1 = tk.Button(root, text="Sayfa 1", command=lambda: show_page("page1"))
button2 = tk.Button(root, text="Sayfa 2", command=lambda: show_page("page2"))
button3 = tk.Button(root, text="Sayfa 3", command=lambda: show_page("page3"))

button1.pack()
button2.pack()
button3.pack()

root.mainloop()