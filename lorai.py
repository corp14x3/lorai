from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os , webbrowser , datetime , feedparser

def speak(text):
    tts = gTTS('{}'.format(text),lang='tr')
    tts.save('lorai.mp3')
    playsound('lorai.mp3')
    os.remove('lorai.mp3')

def lorai():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio=r.listen(source,timeout=0,phrase_time_limit=3)
            command=str(r.recognize_google(audio,language="tr"))
            print(command)

            if datetime.datetime.now().strftime("%H:%M:%S") == '23:30:00':
                speak(text='Tuna üzgünüm ama yatman gerek. İyi geceler!')

            if datetime.datetime.now().strftime("%H:%M:%S") == '07:30:00':
                speak(text='Günaydın hocam!')

            if command in ["WhatsApp'ı aç","WhatsApp'ı açar mısın"]:
                speak(text='Hemen açıyorum.')
                webbrowser.open(url='https://web.whatsapp.com/')
            
            if datetime.datetime.now().strftime("%H:%M:%S") == '07:30:00':
                speak(text='Ders saatin geldi bro.')
                webbrowser.open(url='https://lms.gedik.edu.tr/')

            if command == 'saat kaç':
                saat = datetime.datetime.now().strftime('%H:%M')
                speak(text=('saat' + str(saat)))

            if command == 'Bugün günlerden ne':
                gun = datetime.datetime.now().strftime("%A")
                from googletrans import Translator
                trans = Translator()
                nw = trans.translate(src='auto',dest='tr',text=str(gun))
                speak(text=('Bugün günlerden' + str(nw.text)))
            
            if command == "YouTube'u aç":
                speak(text='tamamdır')
                webbrowser.open(url='https://www.youtube.com/')
            

            if command == 'hava kaç derece':
                parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|34893|Istanbul|")
                parse = parse["entries"][0]["summary"]
                parse = parse.split()
                speak(text=('Hava'+parse[4]+'derece'))
            
        except:
            pass




while True:
    lorai()