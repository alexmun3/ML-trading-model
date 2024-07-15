import os
import shutil
import re
from PIL import Image

def extract_date(filename):
    match = re.search(r'(\d{4}[-_]?\d{2}[-_]?\d{2})', filename)
    if match:
        return match.group(1).replace('-', '').replace('_', '')
    return '00000000'

def show_image(image_path):
    img = Image.open(image_path)
    img.show()

def organize_images(source_dir):
    print(f"Looking for images in: {source_dir}")

    # Ensure the paths for destination directories
    bullish_dir = os.path.join(source_dir, 'bullish_2')
    bearish_dir = os.path.join(source_dir, 'bearish_2')
    uncertain_dir = os.path.join(source_dir, 'uncertain_2')

    os.makedirs(bullish_dir, exist_ok=True)
    os.makedirs(bearish_dir, exist_ok=True)
    os.makedirs(uncertain_dir, exist_ok=True)

    # List all files in the source directory and filter image files
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f)) and 
             f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    files.sort(key=extract_date)
    print(f"Files found in directory (sorted by date): {files}")

    image_count = 0
    for filename in files:
        source_file = os.path.join(source_dir, filename)
        print(f"\nProcessing file: {filename}")
        print(f"Full path to file: {source_file}")

        # Check if the file exists
        if not os.path.exists(source_file):
            print(f"File does not exist: {source_file}")
            continue

        # Show the image
        show_image(source_file)
        
        # Prompt user for classification
        print(f"Classify the image: {filename}")
        classification = input("Enter 'b' for bullish, 'r' for bearish, or 'u' for uncertain: ").strip().lower()
        if classification == 'b':
            dest_dir = bullish_dir
        elif classification == 'r':
            dest_dir = bearish_dir
        else:
            dest_dir = uncertain_dir
        
        # Move the file
        try:
            shutil.move(source_file, os.path.join(dest_dir, filename))
            print(f"Moved {filename} to {dest_dir}")
            image_count += 1
        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")

    if image_count == 0:
        print("No images found to classify.")
    else:
        print(f"\nClassified {image_count} images.")
    
    print("\nSummary of sorted images:")
    for category in [bullish_dir, bearish_dir, uncertain_dir]:
        images = [f for f in os.listdir(category) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        images.sort(key=extract_date)
        print(f"\n{os.path.basename(category).capitalize()}:")
        for image in images:
            print(f"  - {image}")

    print("\nOrganization complete. Check the 'bullish_2', 'bearish_2', and 'uncertain_2' folders.")

# Get the current directory (where the script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script is running from: {current_dir}")

# Print current working directory for additional debugging
print(f"Current working directory: {os.getcwd()}")

# Run the organization
organize_images(current_dir)
