# import youtube from pytube laibrary
from pytube import YouTube
#declare var that include 
link = (input("enter your url: "))
yt = YouTube(link);

#this code download the vedio in resloution 480
stream = yt.streams.get_by_resolution(480).download();

print("download done")