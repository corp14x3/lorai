
from tkinter import messagebox
import os
username = os.getlogin()
command =  input()
if command == 'temizle':
    delete_folder = ["Temp","Prefetch"]
    delete_folder2 = (r"C:\Users\{}\AppData\Local\Temp".format(username))
    files = os.scandir(path=f"{delete_folder2}")
    for file_ in files:
        try:
            os.remove(path=f"{delete_folder2}\{file_.name}")
        except:
            pass
    for i in range(0,len(delete_folder)):
        files = os.scandir(path=f"C:\Windows\{delete_folder[i]}")
        for file_ in files:
            try:
                os.remove(path=f"C:\Windows\{delete_folder[i]}\{file_.name}")
            except:
                pass
    messagebox.showinfo(title="Lorai Clearing System",message="Dosyalar Temizlendi")