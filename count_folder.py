import os

def count_folders_and_empty(directory):
    folder_count = 0
    empty_folder_count = 0
    folder_names = set()  # Set to store folder names
    duplicate_folder_count = 0  # Counter for duplicate folder names

    # Get the list of files and folders in the specified directory
    items = os.listdir(directory)

    # Iterate through the items and count the folders, empty folders, and check for duplicates
    for item in items:
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            folder_count += 1

            # Check if the folder is empty
            if not os.listdir(item_path):
                empty_folder_count += 1

            # Check for duplicate folder names
            if item in folder_names:
                duplicate_folder_count += 1
            else:
                folder_names.add(item)

    return folder_count, empty_folder_count, duplicate_folder_count

# Specify the path to the directory you want to analyze
directory_path = os.path.join(os.getcwd(), 'BK')

# Call the function to count folders, empty folders, and check for duplicates
total_folders, empty_folders, duplicate_folder_count = count_folders_and_empty(directory_path)

print(f"Number of folders in '{directory_path}': {total_folders}")
print(f"Number of empty folders in '{directory_path}': {empty_folders}")
print(f"Number of duplicate folders in '{directory_path}': {duplicate_folder_count}")
