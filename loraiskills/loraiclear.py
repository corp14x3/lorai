import os 

username = os.getlogin()
delete_folder = ["Temp","Prefetch"]
delete_folder2 = (r"C:\Users\{}\AppData\Local\Temp".format(username))


print("----" + delete_folder2+ "----")
files = os.scandir(path=f"{delete_folder2}")
for file_ in files:
    print(file_.name)
    try:
        os.remove(path=f"{delete_folder2}\{file_.name}")
        #size = os.path.getsize(path)
        #print("dosya boyutu :", size)
        print("dosya silindi ✅")
    except:
        print("dosya silinemedi 🅾️")


for i in range(0,len(delete_folder)):
    print("----" + delete_folder[i] + "----")
    files = os.scandir(path=f"C:\Windows\{delete_folder[i]}")
    for file_ in files:
        print(file_.name)
        try:
               
            os.remove(path=f"C:\Windows\{delete_folder[i]}\{file_.name}")
            # size = os.path.getsize(path)
            # print("dosya boyutu :", size)
            print("dosya silindi ✅")
        except:
            print("dosya silinemedi 🅾️")