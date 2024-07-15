import os
import shutil

# Define the source directory where the images are located
source_dir = 'bearish_2'

# Define the target directories for bullish and bearish images
bullish_dir = 'bullish_2'
bearish_dir = 'bearish_2'
consolodation_dir = 'consolidate_2'

# Create target directories if they don't exist
os.makedirs(bullish_dir, exist_ok=True)
os.makedirs(bearish_dir, exist_ok=True)
os.makedirs(consolodation_dir, exist_ok=True)

# Iterate over the files in the source directory
for filename in os.listdir(source_dir):
    # Check if the file is an image by its extension (e.g., .jpg, .png)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Check if 'long' is in the filename
        if 'bullish' in filename.lower():
            # Move the file to the bullish directory
            shutil.move(os.path.join(source_dir, filename), os.path.join(bullish_dir, filename))
        # Check if 'short' is in the filename
        elif 'bearish' in filename.lower():
            # Move the file to the bearish directory
            shutil.move(os.path.join(source_dir, filename), os.path.join(bearish_dir, filename))
        elif 'consolidated' in filename.lower():    
            shutil.move(os.path.join(source_dir, filename), os.path.join(bearish_dir, filename))

print("Images have been sorted successfully.")
