import os
import subprocess
import sys

def export_videos_to_premiere(folder_path):
    # Supported video formats
    video_formats = ('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv')
    
    # Define your auto-editor settings
    cut_by_silence = '--cut-by-silence'  # Use silence detection for cuts
    min_silence_duration = '--min-silence-duration 0.5s'  # Minimum silence duration to detect
    min_silence_volume = '--min-silence-volume -20dB'  # Minimum volume threshold for silence
    export_format = '--export premiere'  # Export settings for Premiere Pro
    frame_margin = '--frame-margin 0'  # ⭐ Reduce to 3 frames around detected silence

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(video_formats):
            file_path = os.path.join(folder_path, filename)
            # Run the auto-editor command
            command = f'auto-editor "{file_path}" --export premiere'
            subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Get the directory of the script/executable
    folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    export_videos_to_premiere(folder_path)

