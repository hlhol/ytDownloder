import pytube

#You can edit the path of folder, but don't edit the r before path.
folder = r"write your folder path "

#Ask user to choose what to download
choice = input("Enter '1' to download a single video or '2' to download a playlist: ")

#If choice is 1, download a single video
if choice == '1':
    link = input("Enter video URL: ")
    yt = pytube.YouTube(link)
    stream = yt.streams.get_by_resolution(480)
    print(f"Downloading {yt.title}...")
    downloaded_file = stream.download()
    if downloaded_file:
    print(f"{yt.title} downloaded successfully!\n")
    else:
        print(f"Failed to download {yt.title}\n")

#If choice is 2, download a playlist
elif choice == '2':
playlist_url = input("Enter playlist URL: ")
playlist = pytube.Playlist(playlist_url)
for video_url in playlist.video_urls:
    youtube = pytube.YouTube(video_url)
    stream = youtube.streams.get_highest_resolution()
    print(f"Downloading {youtube.title}...")
    downloaded_file = stream.download(folder)
    if downloaded_file:
        print(f"{youtube.title} downloaded successfully!\n")
    else:
        print(f"Failed to download {youtube.title}\n");