import os
import re
import shutil
from colorama import Fore, init

init(autoreset=True)

def debug_warning(message):
    print(Fore.YELLOW + message)

def debug_success(message):
    print(Fore.GREEN + message)

def extract_base_title(filename):
    """Kunin ang base title mula sa filename"""
    patterns = [
        # Para sa "Tokyo Revengers - Watch Tagalog Anime Online 5.mp4"
        (r"^(.+?)\s*[-–—]?\s*(?:Watch Tagalog Anime Online|Episode|Ep\.?)\s*\d+", 1),
        # Para sa mga may season marker
        (r"^(.+?)\s*[S|s]\d+", 1),
        # Generic na numero sa dulo
        (r"^(.+?)\s*\d+$", 1)
    ]
    
    for pattern, group in patterns:
        match = re.match(pattern, filename, re.IGNORECASE)
        if match:
            title = match.group(group).strip()
            return re.sub(r"[\-_\.]$", "", title)  # Tanggalin ang trailing separators
    
    return None

def organize_files(source_dir, dry_run=False):
    video_ext = ('.mp4', '.mkv', '.avi', '.mov')
    
    for filename in os.listdir(source_dir):
        if not filename.lower().endswith(video_ext):
            continue

        file_path = os.path.join(source_dir, filename)
        base_name = os.path.splitext(filename)[0]
        
        # Kunin ang base title
        folder_name = extract_base_title(base_name) or "Unknown Anime"
        clean_folder = re.sub(r'[\\/*?:"<>|]', '', folder_name).strip()
        
        target_dir = os.path.join(source_dir, "Organized Anime", clean_folder)
        target_path = os.path.join(target_dir, filename)

        if dry_run:
            debug_success(f"[DRY RUN] Would move: {filename}")
            debug_success(f"          To: {target_path}")
            continue
            
        os.makedirs(target_dir, exist_ok=True)
        shutil.move(file_path, target_path)
        debug_success(f"Moved: {filename}")

if __name__ == "__main__":
    print(Fore.CYAN + "\n=== Anime Folder Organizer ===")
    source = input("Enter directory path: ").strip()
    
    if not os.path.exists(source):
        print(Fore.RED + "Invalid path!")
        exit()

    dry_run = input("Dry run? (y/n): ").lower() == 'y'
    organize_files(source, dry_run)
    print(Fore.GREEN + "\nOrganization complete!")