# 🎬 CINETUNE - Multi-Platform Video Downloader & Converter

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow?logo=python)
![Status](https://img.shields.io/badge/Status-Working-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A simple Python GUI app to download and convert videos from **YouTube**, **Instagram**, and **Facebook**.

---

## 📽️ Preview

![App Screenshot](bg4.png)

---

## 🚀 Features

✅ YouTube Video Downloader (MP4)  
✅ YouTube Audio Converter (MP3)  
✅ Instagram Reels Downloader (Video/Audio)  
✅ Facebook Video Downloader  
✅ Simple GUI using Tkinter  
✅ Background images and platform logos for visual appeal

---

## 🛠️ Tech Stack

- [Python 3.9+](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [pytube](https://pytube.io/)
- [instaloader](https://instaloader.github.io/)
- [FFmpeg](https://ffmpeg.org/)

---

## 📁 Project Structure

```plaintext
converter/
├── main.py               # Launcher GUI with platform options
├── ytcon.py              # YouTube converter window
├── igcon.py              # Instagram reel downloader
├── fb.py                 # Facebook video downloader
├── tempCodeRunnerFile.py # Temporary file (optional)
│
├── logos/                # Platform logo images
│   ├── youtube.png
│   ├── instagram.png
│   ├── facebook.png
│   ├── ytt.jpeg
│   ├── insta.jpg
│   └── fb.jpg
│
├── bg4.png               # Main background image
└── README.md             # This file
Installation
bash
Copy
Edit
pip install pytube3
pip install instaloader
pip install pillow
🔧 FFmpeg is required for Instagram audio extraction.
Download FFmpeg here and add it to system PATH.

💻 How to Run
bash
Copy
Edit
cd path/to/converter
python main.py
✅ This will open the main GUI window where you can select a platform and proceed to download videos or extract audio.

⚙️ Configuration
Ensure your image paths are correct in the .py files.
You may need to replace:

python
Copy
Edit
Image.open(r"D:\projects\converter\logos\youtube.png")
with:

python
Copy
Edit
Image.open("logos/youtube.png")
For better compatibility when uploading to GitHub.

❗ Notes
Only public videos can be downloaded.

Facebook and Instagram require valid URLs (not expired links).

For instaloader, login may be needed for private reels (not implemented here).

YouTube video/audio conversion is resolution-sensitive; handle exceptions gracefully.

📝 License
MIT License.
This project is for educational and personal use only. Respect copyright and terms of each platform.

🤝 Contribute
Pull requests and feature ideas are welcome!
Please open an issue first to discuss what you would like to change.

📬 Contact
Developer: Shivansh Thakur
Email: [shivanshthakur30@gmail.com]