from pytube import YouTube

link = "https://www.youtube.com/watch?v=-mRaQRr83cI"
youtube_1 = YouTube(link)
print(youtube_1.title)
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("Enter : "))
videos[strm].download()
print("Download Succesfully")


