from tkinter import *
from tkinter import messagebox
import instaloader
import os
import subprocess
from PIL import Image as PILImage,ImageTk

root = Tk()
root.title("Instagram Reel Converter")
root.geometry('500x225')
root.maxsize(500,225)

image1=PILImage.open(r"D:\projects\converter\logos\insta.jpg")
photo=ImageTk.PhotoImage(image1)
background_label = Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def back():
    root.destroy()

download_folder = "download"

L = instaloader.Instaloader()

def merge_audio_video(video_file, audio_file, output_file):
    try:
        command = ['ffmpeg', '-i', video_file, '-i', audio_file, '-c', 'copy', output_file]
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"FFmpeg error: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred while merging: {e}")

def download_instagram_reel(url, download_audio=False):
    try:
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        post = instaloader.Post.from_shortcode(L.context, url.split('/')[-2])
        video_file = os.path.join(download_folder, f"{post.shortcode}.mp4")

        messagebox.showinfo("Downloading", "Downloading Reel...")
        L.download_post(post, target=download_folder)

        if download_audio:
            audio_file = os.path.join(download_folder, f"{post.shortcode}.mp3")
            messagebox.showinfo("Converting", "Extracting Audio...")
            subprocess.run(['ffmpeg', '-i', video_file, '-q:a', '0', '-map', 'a', audio_file], check=True, shell=True)
            messagebox.showinfo("Success", "Audio extracted successfully!")
        else:
            messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def download_video():
    url = url_entry.get()
    download_instagram_reel(url, download_audio=False)

def download_audio():
    url = url_entry.get()
    download_instagram_reel(url, download_audio=True)

Label(root, text='Instagram Reel Converter ', font='Arial 15 bold italic', bg='black', fg="white", padx=2, pady=2).place(x=125, y=15)

bt1 = Button(root, text="Download Audio", bd=3, bg='white', fg='black', command=download_audio)
bt1.place(x=188, y=130)

bt2 = Button(root, text="Download Video", bd=3, bg='white', fg='black', command=download_video)
bt2.place(x=189, y=170)

back_button = Button(root, text="BACK",command=back)
back_button.place(x=380,y=180)

url_label = Label(root, text="Enter Instagram Reel URL: ", font="Arial 11 bold italic", bg="white",fg="black")
url_label.place(x=150, y=65)

url_entry = Entry(root, width=50)
url_entry.place(x=95, y=90)

root.mainloop()
