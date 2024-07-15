import os

# Define the directory where the images are located
directory = 'Yiannis sort this out'

# Iterate over the files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image by its extension (e.g., .jpg, .png)
    #if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Create a new filename by removing spaces
        new_filename = filename.replace(' ', '_')
        # Construct full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file, new_file)

print("Filenames have been updated successfully.")
