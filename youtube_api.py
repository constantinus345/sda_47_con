from pytube import YouTube
#pip install pytube
#https://pytube.io/en/latest/user/install.html


def extract_audio(youtube_url, outx = "."):
    yt = YouTube(youtube_url)
    nume_clip = f"{yt.title}.mp3"
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=outx, filename = nume_clip)

Folder = "M:/"
urlx = 'https://www.youtube.com/watch?v=mXyZGcH3zL4'
extract_audio(urlx, outx=Folder)