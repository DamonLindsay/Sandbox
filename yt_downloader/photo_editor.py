import sys

from pytube import YouTube
from sys import argv


def download_video(link):
    try:
        yt = YouTube(link)
        print("Title: ", yt.title)
        print("Views: ", yt.views)

        yd = yt.streams.get_highest_resolution()
        if yd:
            print("Downloading...")
            yd.download("C:\\Users\\User\\Downloads")
            print("Download completed!")
        else:
            print("No streams found for this video.")
    except Exception as e:
        print("An error occurred: ", e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <youtube_link>")
    else:
        link = sys.argv[1]
        download_video(link)
