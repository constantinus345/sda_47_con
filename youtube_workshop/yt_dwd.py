import queue
from threading import Thread, BoundedSemaphore
from pytube import YouTube

def extract_video(youtube_url, outx):
    yt = YouTube(youtube_url)
    nume_clip = f"{yt.title}.mp3".replace("|", "")
    video_stream = yt.streams.get_audio_only()
    try:
        video_stream.download(output_path=outx, filename=nume_clip)
    except Exception as e:
        print(f"Error encountered: {e}")

output_folder = "C:/Users/Mada/Downloads"

urls = ['https://www.youtube.com/watch?v=G6edqEaFJVg',
        'https://www.youtube.com/watch?v=klmBssEYkdU']

def worker():
    while not url_queue.empty():
        url = url_queue.get()
        with sem:
            extract_video(url, outx=output_folder)
            url_queue.task_done()

url_queue = queue.Queue()
for url in urls:
    url_queue.put(url)

max_requests = min(5, len(urls))

sem = BoundedSemaphore(max_requests)
threads = [Thread(target=worker) for _ in range(max_requests)]

for t in threads:
    t.start()
    print(f"Thread {t} started")

for t in threads:
    t.join()
