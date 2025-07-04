import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube
from PIL import Image as PILImage,ImageTk
import subprocess


# Function to download video as MP4
def download_video():
    url = url_entry.get()
    resolution = resolution_var.get()

    try:
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution, file_extension='mp4').first()
        video.download(output_path='download', filename="video")

        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading video:\n{str(e)}")

# Function to convert video to MP3
def convert_to_mp3():
    url = url_entry.get()

    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download(output_path='downloads', filename="audio")

        messagebox.showinfo("Success", "Audio converted to MP3 successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error converting to MP3:\n{str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Converter")
root.geometry("500x300")
root.maxsize(500,300)
def back():
    root.destroy()
    
image1=PILImage.open(r"D:\projects\converter\logos\ytt.jpeg")
photo=ImageTk.PhotoImage(image1)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# URL entry
url_label = tk.Label(root, text="Enter YouTube URL:",bg="white",font="arial 15 bold")
url_label.pack(pady=30)

url_entry = ttk.Entry(root, width=50)
url_entry.pack()

# Resolution selection for video download
# resolution_label = tk.Label(root, text="Select Resolution (for MP4):")
# resolution_label.pack(pady=10)

resolutions = ['720p', '480p', '360p', '240p', '144p']  # Example resolutions
resolution_var = tk.StringVar(root)
resolution_var.set('360p')  # Default resolution

# resolution_menu = ttk.OptionMenu(root, resolution_var, *resolutions)
# resolution_menu.pack()

# Buttons to download video and convert to MP3
download_button = ttk.Button(root, text="Download Video (MP4)", command=download_video)
download_button.pack(pady=10)

convert_button = ttk.Button(root, text="Convert to MP3", command=convert_to_mp3)
convert_button.pack()

back_button = ttk.Button(root, text="BACK",command=back)
back_button.place(x=350,y=250)


root.mainloop()