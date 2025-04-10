import os
import re
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

class AnimeHandler(FileSystemEventHandler):
    def __init__(self, source_dir):
        self.source_dir = source_dir
        self.processed_files = set()

    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def process_file(self, file_path):
        """Maghintay ng 2 segundo bago i-process para maiwasan ang partial files"""
        time.sleep(2)
        
        filename = os.path.basename(file_path)
        if filename in self.processed_files:
            return

        print(Fore.CYAN + f"\nDetected new file: {filename}")
        
        try:
            if self.organize_file(file_path):
                self.processed_files.add(filename)
        except Exception as e:
            print(Fore.RED + f"Error processing {filename}: {str(e)}")

    def organize_file(self, file_path):
        video_ext = ('.mp4', '.mkv', '.avi', '.mov')
        filename = os.path.basename(file_path)
        
        if not filename.lower().endswith(video_ext):
            return False

        base_name = os.path.splitext(filename)[0]
        folder_name = self.extract_title(base_name)
        clean_folder = re.sub(r'[\\/*?:"<>|]', '', folder_name).strip()
        
        target_dir = os.path.join(self.source_dir, "Organized Anime", clean_folder)
        target_path = os.path.join(target_dir, filename)

        os.makedirs(target_dir, exist_ok=True)
        shutil.move(file_path, target_path)
        
        print(Fore.GREEN + f"Moved: {filename} -> {os.path.relpath(target_path)}")
        return True

    def extract_title(self, filename):
        patterns = [
            (r"^(.+?)\s*[-–—]?\s*(?:Watch Tagalog Anime Online|Ep?\.?)\s*\d+", 1),
            (r"^(.+?)\s*[Ss]\d+", 1),
            (r"^(.+?)\s*\d+$", 1)
        ]
        
        for pattern, group in patterns:
            match = re.match(pattern, filename, re.IGNORECASE)
            if match:
                title = match.group(group).strip()
                return re.sub(r"[-_\.]$", "", title)
        
        return "Unknown Anime"

def start_monitoring(path):
    event_handler = AnimeHandler(path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    
    print(Fore.YELLOW + f"\n🚀 Starting monitoring on: {path}")
    print(Fore.YELLOW + "Press Ctrl+C to stop...")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_path = input("Enter folder to monitor: ").strip()
    
    if not os.path.isdir(monitor_path):
        print(Fore.RED + "Invalid directory path!")
        exit(1)

    start_monitoring(monitor_path)