# import youtube from pytube laibrary
from pytube import YouTube;

#import os
import os;

#declare var that include 
link = (input("enter your url: "))
yt = YouTube(link);


#add spacfic location for folder and the r before the path to the program understand the \ backslash.
folder = r"add your path for the folder that you want to save vedio in"

#this code download the vedio in resloution 480.
# you can add spacific folder to save file in.
stream = yt.streams.get_by_resolution(480).download(folder);  




print("download done");