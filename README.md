# 🗂️ Files Organizer

A versatile tool for organizing anime video files with both **manual** and **automatic real-time monitoring** modes. Perfect for managing Bilibili/Tagalog anime downloads!

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://python.org)
[![FFmpeg Required](https://img.shields.io/badge/FFmpeg-Required-orange.svg)](https://ffmpeg.org)

## ✨ Features

- **Dual Modes**
  - 🖱️ **Manual Mode**: Organize existing files in bulk
  - 🔄 **Auto Mode**: Real-time folder monitoring for new files
- **Smart Pattern Recognition**
  - Extracts titles from various filename formats
  - Handles season/episode markers (S1, Episode 12, etc.)
- **Safety Features**
  - Dry run preview
  - Anti-duplicate protection
  - Partial file detection
- **Cross-Platform**
  - Works on Windows, Linux, and Termux (Android)

## 📦 Installation

### Prerequisites
- Python 3.7+
- FFmpeg (for video processing)

# Clone repository
git clone https://github.com/yourusername/files-organizer.git
cd files-organizer

# Install dependencies
pip install -r requirements.txt
# Clone repository
git clone https://github.com/yourusername/files-organizer.git
cd files-organizer

# Install dependencies
pip install -r requirements.txt

Platform-Specific Setup
Platform	Instructions
Termux	pkg install python ffmpeg
Windows	Download FFmpeg and add to PATH
Linux	sudo apt install python3 ffmpeg
 
# 🚀 Usage
Manual Mode
bash
```
python manual_organizer.py
Enter source directory path
```bash

## Choose dry run (y/n)

Files will be moved to Organized Anime subfolder

Auto Mode (Real-Time Monitoring)
bash
```
python auto_organizer.py
```bash
Enter folder to monitor

Script runs continuously

New files auto-organized as they appear

Sample Folder Structure

Copy
```
📂 Source Folder/
├── 📄 Tokyo Revengers - 5.mp4
├── 📄 Demon Slayer Ep12.mkv
└── 📁 Organized Anime/
    ├── 📂 Tokyo Revengers/
    │   └── 📄 Tokyo Revengers - 5.mp4
    └── 📂 Demon Slayer/
        └── 📄 Demon Slayer Ep12.mkv
```bash

🛠️ Troubleshooting
Common Issues	Solutions
FFmpeg not found	Verify FFmpeg installation and PATH
Permission denied	Run as admin/sudo (Linux) or grant storage permission (Termux)
Partial file detection	Wait 5 seconds after file transfer
Duplicate files	Check processed_files.log
Unrecognized filename format	Use manual title input
🤝 Contributing
Fork the repository

Create feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open Pull Request

📜 License
MIT License - see LICENSE for details

Note: This tool is intended for personal media organization. Ensure you have proper rights to modify and organize the files being processed.