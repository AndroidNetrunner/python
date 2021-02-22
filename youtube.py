import pytube

url = "https://www.youtube.com/watch?v=6PvVDcrAUmQ"

youtube = pytube.Youtube(url)
print(youtube)