import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from PIL import Image, ImageTk
import requests
from io import BytesIO


def download_video():
    try:
        link = link_entry.get()
        yt = YouTube(link)
        title_label.config(text="Title: " + yt.title)
        views_label.config(text="Views: " + str(yt.views))

        yd = yt.streams.get_highest_resolution()
        if yd:
            download_label.config(text="Downloading...")
            yd.download("C:\\Users\\User\\Downloads")
            download_label.config(text="Download completed!")
        else:
            messagebox.showerror("Error", "No streams found for this video.")

        # Display thumbnail
        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)
        thumbnail_data = response.content
        image = Image.open(BytesIO(thumbnail_data))
        image.thumbnail((200, 200))  # Resize thumbnail
        thumbnail = ImageTk.PhotoImage(image)
        thumbnail_label.config(image=thumbnail)
        thumbnail_label.image = thumbnail  # Keep reference to the image to avoid garbage collection
    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))


# Create GUI window
root = tk.Tk()
root.title("Youtube Downloader")

# Create and place widgets
link_label = tk.Label(root, text="Enter YouTube link:")
link_label.pack()
link_entry = tk.Entry(root, width=75)
link_entry.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

title_label = tk.Label(root, text="")
title_label.pack()

views_label = tk.Label(root, text="")
views_label.pack()

download_label = tk.Label(root, text="")
download_label.pack()

# Thumbnail label
thumbnail_label = tk.Label(root)
thumbnail_label.pack()

# Run the GUI event loop
root.mainloop()
