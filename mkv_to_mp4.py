import os
import subprocess

def convert_mkv_to_mp4(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mkv"):
            # Construct full file paths
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".mkv", ".mp4"))
            
            # Run ffmpeg command to convert .mkv to .mp4
            command = ['ffmpeg', '-i', input_file, '-codec', 'copy', output_file]
            subprocess.run(command, check=True)
            print(f"Converted {input_file} to {output_file}")


input_folder = './input'
output_folder = './output'
convert_mkv_to_mp4(input_folder, output_folder)
