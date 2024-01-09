import yt_dlp as youtube_dl , sys
try:
    video_url = sys.argv[1]
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl': f"~/Desktop/lorai/downloads/{filename}",
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
except:
    pass