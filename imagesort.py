import os
import shutil

# Define the source directory where the images are located
source_dir = 'Charts to sort out'

# Define the target directories for bullish and bearish images
bullish_dir = 'bullish photos'
bearish_dir = 'bearish photos'

# Create target directories if they don't exist
os.makedirs(bullish_dir, exist_ok=True)
os.makedirs(bearish_dir, exist_ok=True)

# Iterate over the files in the source directory
for filename in os.listdir(source_dir):
    # Check if the file is an image by its extension (e.g., .jpg, .png)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Check if 'long' is in the filename
        if 'long' in filename.lower():
            # Move the file to the bullish directory
            shutil.move(os.path.join(source_dir, filename), os.path.join(bullish_dir, filename))
        # Check if 'short' is in the filename
        elif 'short' in filename.lower():
            # Move the file to the bearish directory
            shutil.move(os.path.join(source_dir, filename), os.path.join(bearish_dir, filename))

print("Images have been sorted successfully.")
