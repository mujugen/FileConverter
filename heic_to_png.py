from heic2png import HEIC2PNG
from PIL import Image
import os 
#import cairosvg


def convert_heic_to_png(input_path, output_path):
    try:
        heic_img = HEIC2PNG(input_path)
        heic_img.save(output_path)
        print(f"Conversion successful: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def convert_png_to_jpg(png_file, jpg_file):
    try:
        # Open the PNG image
        png_image = Image.open(png_file)

        # Convert and save as JPG
        png_image = png_image.convert("RGB")
        png_image.save(jpg_file, "JPEG")
        
        print(f"Conversion successful: {png_file} -> {jpg_file}")
    except Exception as e:
        print(f"Error converting {png_file} to {jpg_file}: {e}")

def convert_png_to_svg(png_file, svg_file):
    try:
        # Convert PNG to SVG using cairosvg
        cairosvg.png2svg(url=png_file, write_to=svg_file)
        print(f"Conversion successful: {png_file} -> {svg_file}")
    except Exception as e:
        print(f"Error converting {png_file} to {svg_file}: {e}")

# Define the input and output directories
input_directory = "./input"
output_directory = "./output"

# Create the directories if they don't exist
os.makedirs(output_directory, exist_ok=True)
os.makedirs(input_directory, exist_ok=True)

# List HEIC files in the input directory
heic_files = [f for f in os.listdir(input_directory) if f.lower().endswith(".heic")]

# Convert HEIC files to PNG
for heic_file in heic_files:
    print("Converting ", heic_file)
    input_path = os.path.join(input_directory, heic_file)
    output_path = os.path.join(output_directory, os.path.splitext(heic_file)[0] + ".png")
    convert_heic_to_png(input_path, output_path)

# List PNG files in the input directory
png_files = [f for f in os.listdir(input_directory) if f.lower().endswith(".png")]

# Convert PNG files to JPG
#for png_file in png_files:
    #print("Converting ", png_file)
    #png_path = os.path.join(input_directory, png_file)
    #jpg_path = os.path.join(output_directory, os.path.splitext(png_file)[0] + ".jpg")
    #svg_path = os.path.join(output_directory, os.path.splitext(png_file)[0] + ".svg")
    #convert_png_to_svg(png_path, svg_path)
    #convert_png_to_jpg(png_path, jpg_path)
