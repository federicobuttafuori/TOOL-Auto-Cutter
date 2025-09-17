import os
import subprocess
import sys

def process_videos(folder_path):
    # Supported video formats
    video_formats = ('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv')
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(video_formats):
            file_path = os.path.join(folder_path, filename)
            # Run the auto-editor command
            command = f'auto-editor "{file_path}"'
            subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Get the directory of the script/executable
    folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    process_videos(folder_path)
