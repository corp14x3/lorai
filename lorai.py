from playsound import playsound
from gtts import gTTS
from flask import Flask , request , render_template

import os , webbrowser , datetime , feedparser , sqlite3
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

    def loraimain(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio=r.listen(source,timeout=0,phrase_time_limit=3)
                command=str(r.recognize_google(audio,language="tr"))
                last = command.split(" ")
                print(command,last)

                if datetime.datetime.now().strftime("%H:%M:%S") == '23:30:00':
                    lorai.speak(text='Tuna üzgünüm ama yatman gerek. İyi geceler!')

                if datetime.datetime.now().strftime("%H:%M:%S") == '07:30:00':
                    lorai.speak(text='Günaydın hocam!')

                if command in ["WhatsApp'ı aç","WhatsApp'ı açar mısın"]:
                    lorai.speak(text='Hemen açıyorum.')
                    webbrowser.open(url='https://web.whatsapp.com/')

                if command == 'saat kaç':
                    saat = datetime.datetime.now().strftime('%H:%M')
                    lorai.speak(text=('saat' + str(saat)))

                if command == 'Bugün günlerden ne':
                    gun = datetime.datetime.now().strftime("%A")
                    from googletrans import Translator
                    trans = Translator()
                    nw = trans.translate(src='auto',dest='tr',text=str(gun))
                    lorai.speak(text=('Bugün günlerden' + str(nw.text)))

                if command == "YouTube'u aç":
                    lorai.speak(text='tamamdır')
                    webbrowser.open(url='https://www.youtube.com/')

                if last[-1] == "ara":
                    last.remove("ara")
                    print(last)
                    search = ' '.join(last)
                    webbrowser.open(url=f"https://www.google.com/search?q={search}")
                    last.clear()

                if command == 'hava kaç derece':
                    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|34893|Istanbul|")
                    parse = parse["entries"][0]["summary"]
                    parse = parse.split()
                    lorai.speak(text=('Hava'+parse[4]+'derece'))

            except:

                pass


lorai=Lorai()

while True:
    lorai.loraimain()