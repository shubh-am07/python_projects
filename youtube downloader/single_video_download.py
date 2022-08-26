from pytube import YouTube

link = "https://www.youtube.com/shorts/plEJAV3SCyc"
youtube_1 = YouTube(link)

#print(youtube_1.title)
#print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all() #All format

#videos = youtube_1.streams.filter(only_audio=True) #only Audio

vid = list(enumerate(videos))

for i in vid:
    print(i)

print()
strm = int(input("Enter :"))
videos[strm].download()
print("Successfully")