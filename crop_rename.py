import os
import shutil
from PIL import Image
import argparse

def crop_and_save_images(source_folder, target_folder, crop_box):
    # Ensure the target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # List all files in the source folder
    files = os.listdir(source_folder)

    for file_name in files:
        # Check if the file is an image (you can customize the file extension check)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Load the image
            image_path = os.path.join(source_folder, file_name)
            img = Image.open(image_path)

            # Crop the image
            cropped_img = img.crop(crop_box)

            # Save the cropped image to the target folder
            target_path = os.path.join(target_folder, file_name)
            cropped_img.save(target_path)

def copy_and_rename_files(source_folder, destination_folder):
    # List all files in the source folder
    files = os.listdir(source_folder)

    # Iterate through each file and copy/rename it
    for old_name in files:
        # Construct the new name by adding a prefix
        #new_name = old_name[:10] + old_name[13:-4] + '.0.png'
        new_name = old_name[:-4] + '.0.png'


        # Build the full file paths
        old_path = os.path.join(source_folder, old_name)
        new_path = os.path.join(destination_folder, new_name)

        # Copy the file to the destination folder
        shutil.copy2(old_path, new_path)

def main():
    parser = argparse.ArgumentParser(description='Crop, copy/rename images.')

    # Add command line arguments
    parser.add_argument('--source-folder', help='Path to the source folder containing images')
    parser.add_argument('--target-folder', help='Path to the target folder to save cropped images')
    parser.add_argument('--crop-left', type=int, default=0, help='Left coordinate of the crop box')
    parser.add_argument('--crop-upper', type=int, default=0, help='Upper coordinate of the crop box')
    parser.add_argument('--crop-right', type=int, default=968, help='Right coordinate of the crop box')
    parser.add_argument('--crop-lower', type=int, default=600, help='Lower coordinate of the crop box')

    # Parse the command line arguments
    args = parser.parse_args()

    # Specify the crop box based on command line arguments
    crop_box = (args.crop_left, args.crop_upper, args.crop_right, args.crop_lower)

    # Call the crop_and_save_images function
    crop_and_save_images(args.source_folder, args.target_folder, crop_box)
    # Call the copy_and_rename_files function
    copy_and_rename_files(args.target_folder, args.target_folder)

if __name__ == "__main__":
    main()
