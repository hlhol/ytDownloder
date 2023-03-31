import pytube;

#you can edit the path of folder, but don't edit the r before path.
folder = r"write your folder path ";

# Set the URL of the playlist to download by input
playlist_url = input("enter url: ");

# Create a Playlist object using the pytube library
playlist = pytube.Playlist(playlist_url);

# Loop through each video in the playlist and download it
for video_url in playlist.video_urls:
    # Create a YouTube object for the video
    youtube = pytube.YouTube(video_url);

    # Select the 480 resolution stream
    stream = youtube.streams.get_by_resolution(480);

    # Download the stream
    print(f"Downloading {youtube.title}...");  #youtube.title is to get vedio title and print it.
    stream.download(folder); #add spacific location to downloded vedio.
    print(f"{youtube.title} downloaded successfully!\n") #print dwnload 