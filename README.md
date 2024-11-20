# Resizing-Input-and-Output-Images
# Image Resizer Script

This script resizes images in a specified input folder and saves the resized images in a new output folder. The images are resized to a fixed size of 256x256 pixels.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

You can install the required library by running:

```bash
pip install Pillow
 Usage

    Set the input_folder variable to the directory where your original images are located.
    Set the output_folder variable to the directory where you want to save the resized images.
    Run the script. It will process all .jpg, .jpeg, and .png files in the input folder and save the resized images in the output folder.

Example

input_folder = 'C:/Users/ayzeg/Desktop/merged dataset/input'
output_folder = 'C:/Users/ayzeg/Desktop/merged dataset/input resized'
size = (256, 256)

This will resize all images in the input folder to 256x256 pixels and store them in the input resized folder.
License

MIT License

Copyright (c) [2024] [ayoub zangivan]
