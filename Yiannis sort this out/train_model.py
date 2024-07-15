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
    
    os.makedirs(os.path.join(source_dir, 'bullish'), exist_ok=True)
    os.makedirs(os.path.join(source_dir, 'bearish'), exist_ok=True)
    os.makedirs(os.path.join(source_dir, 'uncertain'), exist_ok=True)

    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f)) and 
             f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    files.sort(key=extract_date)
    print(f"Files found in directory (sorted by date): {files}")

    image_count = 0
    for filename in files:
        source_file = os.path.join(source_dir, filename)
        print(f"\nProcessing file: {filename}")
        
        # Show the image
        show_image(source_file)
        
        # Prompt user for classification
        print(f"Classify the image: {filename}")
        classification = input("Enter 'b' for bullish, 'r' for bearish, or 'u' for uncertain: ").strip().lower()
        if classification == 'b':
            dest_dir = os.path.join(source_dir, 'bullish')
        elif classification == 'r':
            dest_dir = os.path.join(source_dir, 'bearish')
        else:
            dest_dir = os.path.join(source_dir, 'uncertain')
        
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
    for category in ['bullish', 'bearish', 'uncertain']:
        folder_path = os.path.join(source_dir, category)
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        images.sort(key=extract_date)
        print(f"\n{category.capitalize()}:")
        for image in images:
            print(f"  - {image}")

    print("\nOrganization complete. Check the 'bullish', 'bearish', and 'uncertain' folders.")

# Get the current directory (where the script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script is running from: {current_dir}")

# Run the organization
organize_images(current_dir)