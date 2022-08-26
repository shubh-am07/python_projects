from pytube import Playlist

py = Playlist("url of playlist")

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()

print("Download Successfully")