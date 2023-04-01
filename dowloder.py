import pytube;

print("Enter  1 to download playlist and enter 2 to download playlist");

num = input('enter your choise: ');

if num == 1:
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

        # Select the high resolution stream
        stream = youtube.streams.get_highest_resolution();

        # Download the stream
        print(f"Downloading {youtube.title}...");  #youtube.title is to get vedio title and print it.
        stream.download(folder); #add spacific location to downloded vedio.
        print(f"{youtube.title} downloaded successfully!\n") #print dwnload 

elif num == 2:
    yt = pytube.YouTube(link);

    print(f"Downloading {youtube.title}...");
    stream = yt.streams.get_by_resolution(480).download();
    print(f"{youtube.title} downloaded successfully!\n") #print dwnload 


    print("download done")
