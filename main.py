import os
import shutil
from datetime import datetime, timedelta
from PIL import Image
from PIL.ExifTags import TAGS


def get_date_taken(file_path):
    try:
        image = Image.open(file_path)
        exif = {TAGS[k]: v for k, v in image._getexif().items() if k in TAGS}
        date_str = exif.get('DateTimeOriginal', None)
        if date_str:
            return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
    except:
        pass

    # If EXIF data is not available, use file modification time
    return datetime.fromtimestamp(os.path.getmtime(file_path))


def sort_photos(source_dir, destination_dir):
    # Get all image files
    image_files = [f for f in os.listdir(source_dir) if f.lower().endswith(('.png', '.arw', '.jpg', '.jpeg', '.gif'))]

    # Sort files by date taken
    sorted_files = sorted(image_files, key=lambda x: get_date_taken(os.path.join(source_dir, x)))

    if not sorted_files:
        print("No image files found in the source directory.")
        return

    current_group = []
    current_group_start_date = get_date_taken(os.path.join(source_dir, sorted_files[0]))

    for file in sorted_files:
        file_date = get_date_taken(os.path.join(source_dir, file))

        if not current_group or (file_date - current_group_start_date).days <= 4:
            current_group.append(file)
        else:
            # Move current group to a new folder
            folder_name = current_group_start_date.strftime('%Y-%m-%d')
            folder_path = os.path.join(destination_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            for group_file in current_group:
                shutil.move(os.path.join(source_dir, group_file), os.path.join(folder_path, group_file))

            # Start a new group
            current_group = [file]
            current_group_start_date = file_date

    # Move the last group
    if current_group:
        folder_name = current_group_start_date.strftime('%Y-%m-%d')
        folder_path = os.path.join(destination_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for group_file in current_group:
            shutil.move(os.path.join(source_dir, group_file), os.path.join(folder_path, group_file))

    print("Photo sorting completed.")


# Usage
source_directory = 'E:/sony2024'
destination_directory = 'E:/sony2024/sorted'
sort_photos(source_directory, destination_directory)
