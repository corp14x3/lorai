from playsound import playsound
from gtts import gTTS
import os , webbrowser , datetime , sqlite3 , googletrans , subprocess , pystray , threading
import speech_recognition as sr
from PIL import Image
from pystray import MenuItem as item

con = sqlite3.connect("lorai.db", check_same_thread=False)
cursor = con.cursor()

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

                if command == 'saat kaç':
                    saat = datetime.datetime.now().strftime('%H:%M')
                    lorai.speak(text=('saat' + str(saat)))

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

            except:
                print('Herhangibi bir ses yok.')
           
lorai=Lorai()


def on_quit():
    icon.visible = False
    icon.stop()
def guilorai():
    subprocess.Popen(r"C:\Users\corp1\Desktop\lorai\loraisite.py",shell=True)
    webbrowser.open(url="http://localhost:7432/shortcuts")
image = Image.open("./static/media/infinity-symbol-clipart-download-best-infinity-14.png")
menu = (
    item('LorAI', guilorai),
    item('Quit', on_quit)
)

icon = pystray.Icon("Lor(A)I", image, "Lorai GUI", menu)


def run_lorai():
    while True:
        lorai.loraimain()

lorai_thread = threading.Thread(target=run_lorai)
lorai_thread.start()

icon.run()