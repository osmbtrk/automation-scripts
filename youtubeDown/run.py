import os
from pytube import YouTube

# Open the text file containing YouTube links
with open('/storage/emulated/0/youtube/download.txt', 'r') as file:
    links = file.readlines()

# Loop through each link and download the video
for link in links:
    try:
        yt = YouTube(link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download('/storage/emulated/0/youtube/vid')
        print('Video downloaded successfully!')

        # Remove the downloaded link from the text file
        with open('/storage/emulated/0/youtube/download.txt', 'r') as file:
            lines = file.readlines()
        with open('/storage/emulated/0/youtube/download.txt', 'w') as file:
            for line in lines:
                if line.strip('\n') != link.strip('\n'):
                    file.write(line)
        print('Link removed from the text file.')
    except Exception as e:
        print(f'Error downloading video: {e}')

