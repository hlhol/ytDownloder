# import youtube from pytube laibrary
from pytube import YouTube

link = (input("enter your url: "))
yt = YouTube(link);

stream = yt.streams.get_by_resolution(480).download();

print("download done")