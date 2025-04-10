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

```bash
# Clone repository
git clone https://github.com/yourusername/files-organizer.git
cd files-organizer

# Install dependencies
pip install -r requirements.txt
```

### Platform-Specific Setup

| Platform  | Instructions                                                                 |
|-----------|-----------------------------------------------------------------------------|
| **Termux**| `pkg install python ffmpeg`                                                |
| **Windows**| [Download FFmpeg](https://www.gyan.dev/ffmpeg/builds/) and add to PATH     |
| **Linux** | `sudo apt install python3 ffmpeg`                                          |

## 🚀 Usage

### Manual Mode
```bash
python manual_organizer.py
```
1. Enter source directory path
2. Choose dry run (y/n)
3. Files will be moved to `Organized Anime` subfolder

### Auto Mode (Real-Time Monitoring)
```bash
python auto_organizer.py
```
1. Enter folder to monitor
2. Script runs continuously
3. New files auto-organized as they appear

**Sample Folder Structure**
```
📂 Source Folder/
├── 📄 Tokyo Revengers - 5.mp4
├── 📄 Demon Slayer Ep12.mkv
└── 📁 Organized Anime/
    ├── 📂 Tokyo Revengers/
    │   └── 📄 Tokyo Revengers - 5.mp4
    └── 📂 Demon Slayer/
        └── 📄 Demon Slayer Ep12.mkv
```

## 🛠️ Troubleshooting

| Common Issues               | Solutions                                 |
|-----------------------------|------------------------------------------|
| FFmpeg not found            | Verify FFmpeg installation and PATH      |
| Permission denied           | Run as admin/sudo or grant permissions   |
| Partial file detection      | Wait 5 seconds after file transfer       |
| Unrecognized filename format| Use manual title input                   |

## 🤝 Contributing
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📜 License
MIT License - see [LICENSE](LICENSE) for details

---

**Note**: This tool is intended for personal media organization. Ensure you have proper rights to modify and organize the files being processed.