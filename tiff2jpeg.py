import os
from tqdm import tqdm
import concurrent.futures
import imageio.v2 as imageio  # Import imageio's v2 module

# Define your directories
input_dir = "your input directory"
output_dir = "your output directory"

# Find all .tiff files in input_dir
tiff_files = [os.path.join(root, name)
              for root, dirs, files in os.walk(input_dir)
              for name in files
              if name.endswith((".tiff", ".tif"))]

# Set to remember directories
created_dirs = set()

# Function to process each file
def process_file(file_path):
    new_file_path = file_path.replace(input_dir, output_dir)
    new_dir_path = os.path.dirname(new_file_path)

    # Create directory only if it hasn't been created before
    if new_dir_path not in created_dirs:
        os.makedirs(new_dir_path, exist_ok=True)
        created_dirs.add(new_dir_path)

    # Using imageio.v2 for reading and saving images
    image = imageio.imread(file_path)
    new_file_path = os.path.splitext(new_file_path)[0] + '.jpg'
    imageio.imsave(new_file_path, image, quality=95)

# Use ProcessPoolExecutor or ThreadPoolExecutor to process files concurrently
# Uncomment the executor you want to use
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:  # Adjust max_workers as per your observations
    # with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:  # Adjust max_workers as per your observations
    list(tqdm(executor.map(process_file, tiff_files), total=len(tiff_files), ncols=70))
