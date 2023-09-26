from heic2png import HEIC2PNG
import os 

# Define a function to convert HEIC to PNG
def convert_heic_to_png(input_path, output_path):
    try:
        heic_img = HEIC2PNG(input_path)
        heic_img.save(output_path)
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

# Define the input and output directories
input_directory = "./input"
output_directory = "./output"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List HEIC files in the input directory
heic_files = [f for f in os.listdir(input_directory) if f.lower().endswith(".heic")]

# Loop through HEIC files and convert them to PNG
for heic_file in heic_files:
    input_path = os.path.join(input_directory, heic_file)
    output_path = os.path.join(output_directory, os.path.splitext(heic_file)[0] + ".png")
    convert_heic_to_png(input_path, output_path)
