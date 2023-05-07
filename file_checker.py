import os, time

folder_path = "./test_folder"

# Check if folder exists
if not os.path.exists(folder_path):
    print(f"Folder does not exist: {folder_path}")
    exit()  # Exit program


while True:
    # Collect files from folder_path
    files = os.listdir(folder_path)

    # break if not files
    if not files:
        print("Couldn't find files in the folder :((")
        break