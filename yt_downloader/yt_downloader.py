import os.path
import time
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from PIL import Image, ImageTk
import requests
import threading
from io import BytesIO


def search_video():
    try:
        link = link_entry.get()
        yt = YouTube(link)
        title_label.config(text="Title: " + yt.title)
        views_label.config(text="Views: " + str(yt.views))

        # Display thumbnail
        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)
        thumbnail_data = response.content
        image = Image.open(BytesIO(thumbnail_data))
        image.thumbnail((200, 200))  # Resize thumbnail
        thumbnail = ImageTk.PhotoImage(image)
        thumbnail_label.config(image=thumbnail)
        thumbnail_label.image = thumbnail  # Keep reference to the image to avoid garbage collection

        #  Enable download button
        download_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))


def download_video():
    global download_finished

    def download():
        try:
            link = link_entry.get()
            yt = YouTube(link)

            yd = yt.streams.get_highest_resolution()
            if yd:
                download_label.config(text="Downloading...")
                yd.download("C:\\Users\\User\\Downloads")
                download_label.config(text="Download completed!")
            else:
                messagebox.showerror("Error", "No streams found for this video.")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e))

    # Start a new thread to perform the download operation
    threading.Thread(target=download).start()

    # Update the download progress and speed
    update_download_status()


def update_download_status():
    try:
        link = link_entry.get()
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        if yd:
            while not download_finished:
                total_size = yd.filesize
                filesize_downloaded = os.path.getsize(f"C:\\Users\\User\\Downloads\\{yt.title}")
                progress = (filesize_downloaded / total_size) * 100 if total_size else 0
                download_label.config(
                    text=f"Downloading... {progress:.2f}% - {filesize_downloaded} / {total_size} bytes - ")
                root.update_idletasks()  # Update the GUI
                time.sleep(1)  # Update every second
    except Exception as e:
        download_label.config(text="Error: " + str(e))


# Initialize global variables
download_finished = False

# Create GUI window
root = tk.Tk()
root.title("Youtube Downloader")

# Create and place widgets
link_label = tk.Label(root, text="Enter YouTube link:")
link_label.pack()
link_entry = tk.Entry(root, width=75)
link_entry.pack()

search_button = tk.Button(root, text="Search", command=search_video)
search_button.pack()

title_label = tk.Label(root, text="")
title_label.pack()

views_label = tk.Label(root, text="")
views_label.pack()

# Thumbnail label
thumbnail_label = tk.Label(root)
thumbnail_label.pack()

# Download button
download_button = tk.Button(root, text="Download", command=download_video, state=tk.DISABLED)
download_button.pack()

download_label = tk.Label(root, text="")
download_label.pack()

# Run the GUI event loop
root.mainloop()
