import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube
from PIL import Image as PILImage,ImageTk
import requests

# Function to download the video
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    
   
    if "facebook.com" not in url:
        messagebox.showerror("Error", "Please enter a valid Facebook video URL")
        return

    
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        
       
        save_path = filedialog.askdirectory()
        if not save_path:
            return

        
        messagebox.showinfo("Downloading", "Video is being downloaded...")
        video_stream.download(output_path=save_path)
        messagebox.showinfo("Success", "Video downloaded successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Facebook Video Downloader")
root.geometry('500x225')
root.maxsize(500,225)
image1=PILImage.open(r"D:\projects\converter\logos\fb.jpg")
photo=ImageTk.PhotoImage(image1)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def back():
    root.destroy()

# URL label and entry
url_label = tk.Label(root, text="Enter Facebook Video URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

back_button = tk.Button(root, text="BACK",command=back)
back_button.place(x=380,y=180)

# Run the Tkinter main loop
root.mainloop()