from playsound import playsound
from gtts import gTTS
from flask import Flask , request , render_template

import os , webbrowser , datetime , sqlite3 , googletrans
import speech_recognition as sr

print("Lorai System Controller")

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
                command=str(r.recognize_google(audio,language="tr"))
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

                elif command == 'Bilgisayarı kapat':
                    os.system("shutdown /s /t 0")
                
                elif command == 'Bilgisayarı yeniden başlat':
                    os.system("shutdown /r /t 0")
                
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
           




while True:
    lorai=Lorai()
    lorai.loraimain()