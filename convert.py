import pdb
import subprocess
import glob
import os


def convert_video(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,  # Input file
        '-c:v', 'libx264',  # Video codec
        '-preset', 'fast',  # Preset for encoding speed/quality trade-off
        '-crf', '23',  # Constant Rate Factor (quality level, where lower is better)
        '-c:a', 'aac',  # Audio codec
        '-b:a', '192k',  # Audio bitrate
        output_file  # Output file
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print("Conversion successful!")
    except subprocess.CalledProcessError:
        print("An error occurred during conversion.")


video_files  = glob.glob(os.path.join("./static/speaker/*/*.mp4"))
output_dir = "./static/speaker_"
os.makedirs(output_dir,exist_ok=True)

for vv in video_files:
    dir_name = vv.split("/")[-2]
    file_name = vv.split("/")[-1]
    output_path = os.path.join(output_dir, dir_name,file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Call the function to convert the video
    convert_video(vv, output_path)
