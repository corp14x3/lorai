from playsound import playsound
from gtts import gTTS
import os , webbrowser , datetime , sqlite3 , googletrans , subprocess , pystray , threading , pyautogui , keyboard , time
import speech_recognition as sr
from PIL import Image
from pystray import MenuItem as item
from tkinter import messagebox
from selenium import webdriver
import random, pymem , requests as r , yt_dlp as youtube_dl

if os.name == "posix":
    print("We will do some optimize for ur Linux / Android")
    
if os.name == "nt":
    print("We will do some optimize for ur Windows")

class Lorai():
    def __init__(self):
        pass
    def speak(self,text):
        tts = gTTS('{}'.format(text),lang='tr')
        tts.save('lorai.mp3')
        playsound('lorai.mp3')
        os.remove('lorai.mp3')

    def speak_en(self,text):
        tts = gTTS('{}'.format(text),lang='en')
        tts.save('lorai.mp3')
        playsound('lorai.mp3')
        os.remove('lorai.mp3')  

    def loraimain(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio=r.listen(source,timeout=0,phrase_time_limit=3)
                command = str(r.recognize_google(audio,language="tr"))
                command = command.lower()
                last = command.split(" ")
                print(command,last)

                if command == 'example':
                    pass

                elif last[0] == "ara":
                    last.remove("ara")
                    search = ' '.join(last)
                    print(last)
                    if '.' in list(search):
                        webbrowser.open(url=f"https://{search}")
                    else:
                        webbrowser.open(url=f"https://www.google.com/search?q={search}")
                    last.clear()

                elif command == 'bilgisayarı kapat':
                    os.system("shutdown /s /t 0")
                
                elif command == 'bilgisayarı yeniden başlat':
                    os.system("shutdown /r /t 0")

                elif last[0] == 'aç':
                    liste = cursor.execute("SELECT * FROM programsc WHERE pn = ?",[str(last[1])])
                    data = liste.fetchall()
                    subprocess.Popen(r"".join(data[0][1]),shell=True)

                elif last[0] == 'çevir':
                    last.remove('çevir')
                    translator = googletrans.Translator()
                    question = " ".join(last)
                    print(question)
                    answerwrite = translator.translate(text=question,src='tr',dest='en')
                    print(answerwrite.text)
                    lorai.speak_en(text=answerwrite.text)

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


                import loraicommands
                loraicommands


            except:
                print('Herhangibi bir ses yok.')
            
           
lorai=Lorai()


def on_quit():
    icon.visible = False
    icon.stop()

image = Image.open("./static/media/lorai.png")
menu = (
    item('LorAI', "pass"),
    item('Quit', on_quit)
)

icon = pystray.Icon("Lor(A)I", image, "Lorai GUI", menu)


def run_lorai():
    while True:
        l = lorai.loraimain()

lorai_thread = threading.Thread(target=run_lorai)
lorai_thread.start()

icon.run()





















username = os.getlogin()
con = sqlite3.connect("lorai.db", check_same_thread=False) 
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS programsc (pn TEXT, pw TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS cmh (command TEXT, file TEXT)")


def loraiprogram():
    liste = cursor.execute("SELECT * FROM programsc")
    data = liste.fetchall()
    progn = request.form.get("programname")
    progw = request.form.get("programway")
    cursor.execute("INSERT INTO programsc VALUES(?,?)",(progn,progw))
    con.commit()

def loraiprogramd():
    liste = cursor.execute("SELECT * FROM programsc")
    data = liste.fetchall()
    progn = request.form.get("programname")
    cursor.execute("DELETE FROM programsc WHERE pn = ?",[progn])
    con.commit()


def loraiyd():
    try:
        video_url = request.form.get("link")
        video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
        filename = f"{video_info['title']}.mp3"
        options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl': f"~/Desktop/lorai/downloads/{filename}",
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
            time.sleep(2)
    except:
        time.sleep(2)

def loraicmh():
    liste = cursor.execute("SELECT * FROM cmh")
    data = liste.fetchall()
    if request.method == "POST":
        command = request.form.get("command")
        if "add" in request.form:
            with open(file=f"commands/{command}.py",mode="x",encoding="utf-8") as f:
                pass
            with open(file="loraicommands.py",mode="+a",encoding="utf-8") as f:
                f.writelines(f"\nfrom commands.{command} import *")
            cursor.execute("INSERT INTO cmh VALUES(?,?)",(command,f".command/{command}.py"))
            con.commit()
        if "delete" in request.form:
            cursor.execute("DELETE FROM cmh WHERE command = ?",[command])
            os.remove(path=f"commands/{command}.py")
            con.commit()


def loraicset():
            os.system("powercfg /DUPLICATESCHEME e9a42b02-d5df-448d-aa00-03f14749eb61")
            flash("Nihai performans olusturuldu.")
            try:
                os.system('netsh interface ipv4 set dns "Wi-Fi" static 1.1.1.1 primary')#netsh interface ip add dns name="Wi-Fi" addr=8.8.8.8  netsh interface ip add dns name="Wi-Fi" addr=8.8.4.4 index=2
                os.system('netsh interface ipv4 add dns "Wi-Fi" 1.0.0.1 index=2')
                os.system('netsh interface ipv6 set dns "Wi-Fi" static 2606:4700:4700::1111 primary')
                os.system('netsh interface ipv6 add dns "Wi-Fi" 2606:4700:4700::1001 index=2')
            except:
                pass
            try:
                os.system('netsh interface ipv4 set dns "Ethernet" static 1.1.1.1 primary')
                os.system('netsh interface ipv4 set dns "Ethernet" static 1.0.0.1 index=2')
                os.system('netsh interface ipv6 set dns "Ethernet" static 2606:4700:4700::1111 primary')
                os.system('netsh interface ipv6 set dns "Ethernet" static 2606:4700:4700::1001 index=2')
            except:
                pass