import os, json
from PIL import Image, ExifTags

# r = raw string
folder_path = r"D:\Work\_PythonSuli\kezdo_230506\photos"
assert os.path.exists(folder_path), f"Nem létezik az útvonal: {folder_path}"
assert os.path.isdir(folder_path), f"A megadott útvonal nem könyvtár: {folder_path}"


files = os.listdir(folder_path)
assert len(files) != 0, f"A könyvtár üres: {folder_path}"

# collect data from images
photo_data = {}
for file_name in files:
    full_path = os.path.join(folder_path, file_name)

    # open image in memory
    img = Image.open(full_path)

    # get meta data
    exif_data = img._getexif()
    if not exif_data:
        continue
    
    # add data to photo_data dict
    photo_data[file_name] = {"path": full_path, "date": exif_data.get(0x9003), "camera": exif_data.get(0x0110), "iso": exif_data.get(0x8827), "size": img.size}

# write our photo_data.json
with open("photo_data.json", "w") as data_file:
    json.dump(photo_data, data_file)

# read json file
with open("photo_data.json") as data_file:
    data = json.load(data_file)