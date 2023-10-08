if command == 'saat kaç':
    saat = datetime.datetime.now().strftime('%H:%M')
    lorai.speak(text=('saat' + str(saat)))