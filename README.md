# 🎬 CINETUNE - Multi-Platform Video Downloader & Converter

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow?logo=python)
![Status](https://img.shields.io/badge/Status-Working-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> CINETUNE is a Python GUI-based application that lets users download and convert videos from **YouTube**, **Instagram**, and **Facebook** using a visually appealing interface built with Tkinter.

---

## 📽️ Preview

> Make sure to include the `bg4.png` file in your repository for this image to appear.

![App Screenshot](bg4.png)

---

## 🚀 Features

### 🟥 YouTube Converter (`ytcon.py`)
- Download videos in different resolutions (MP4)
- Convert videos to MP3 audio format
- Simple and responsive interface

### 🟪 Instagram Reel Converter (`igcon.py`)
- Download Instagram reels directly via link
- Option to extract audio (MP3) using FFmpeg
- Automatically organizes files in a `download/` folder

### 🟦 Facebook Downloader (`fb.py`)
- Download Facebook public videos using a valid URL
- Custom folder selection for saving files

---

## 🛠️ Requirements

Install the required Python libraries:

```bash
pip install pytube3
pip install instaloader
pip install pillow

---
```
### 📂 Project Structure
```
converter/
├── main.py               # Main app launcher window
├── ytcon.py              # YouTube converter GUI
├── igcon.py              # Instagram reel downloader GUI
├── fb.py                 # Facebook video downloader GUI
├── tempCodeRunnerFile.py # Temporary file (optional)
│
├── logos/                # Folder with platform logos
│   ├── youtube.png
│   ├── instagram.png
│   ├── facebook.png
│   ├── ytt.jpeg
│   ├── insta.jpg
│   └── fb.jpg
│
├── bg4.png               # Background image for the main GUI
└── README.md             # This file

---
```
### ▶️ How to Run the App

Open your terminal or command prompt.

Navigate to your project directory:

```bash
cd D:\projects\converter
``` 
---

### Launch the main application:
python main.py

This will open a graphical interface with three platform buttons. Click on any platform to open its specific video/audio downloader.

### 👨‍💻 Author

Shivansh Thakur
GitHub: @shivanshthakur55