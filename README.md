# Photo Sorting Script

This Python script automatically sorts photos into folders based on the time distance between them. If the time distance between photos is greater than 4 days, it moves them to a new folder named after the date of the first image in that group.

## Features

- Sorts photos based on the date they were taken
- Uses EXIF data when available, falls back to file modification date
- Creates folders named with the date of the first photo in each group
- Handles various image formats (PNG, JPG, JPEG, GIF)

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required Pillow library:

   pip install Pillow

## Usage

1. Place the script in a convenient location.
2. Modify the following lines at the bottom of the script with your desired source and destination directories:

   source_directory = '/path/to/source/directory'
   destination_directory = '/path/to/destination/directory'

3. Run the script:

   python photo_sorter.py

## How It Works

The script performs the following steps:

1. Scans the source directory for image files.
2. Sorts the files based on the date they were taken.
3. Groups photos that were taken within 4 days of each other.
4. Creates a new folder for each group, named after the date of the first photo in that group.
5. Moves the photos to their respective folders.

## Caution

- This script moves files from your source directory. It's recommended to backup your photos before running the script.
- Ensure you have write permissions for both the source and destination directories.

## Customization

You can modify the time threshold (currently set to 4 days) by changing the following line in the script:

if not current_group or (file_date - current_group_start_date).days <= 4:

## Contributing

Feel free to fork this project and submit pull requests with any enhancements.

## License

This project is open source and available under the [MIT License](LICENSE).
