from pytube import Playlist

url_channel = 'https://www.youtube.com/watch?v=mEdCHkBEnV4&list=PLGmx5QgG0FlYYhUk4_1nLnkw7AaHYWh5F&ab_channel=DorianDevelops'
p = Playlist(url_channel)
#print(c.channel_name)
# for url in c.video_urls:
#     print(url)

for url in p.video_urls:
    print(url)