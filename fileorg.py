import pathlib
import time
import os

#directory thats being used
#put your pcs name in the -name- without the --
direcory = "C:/Users/-name-/Downloads"

categories = {
    '1-Images': ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.bpg', 'svg'],
    '2-Videos': ['.webm', '.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg', '.3gp'],
    '3-Documents': ['.txt', '.oxps', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods', '.odt', '.pwi', '.xsn', '.xps', '.dotx', '.docm', '.dox', '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt', 'pptx'],
    '4-Zips': ['.zip', '.rar', '.tar', '.iso', '.7z', '.gz'],
    '5-Pdfs': ['.pdf']
}
    
for category in ['1-Images', '2-Videos', '3-Documents', '4-Zips', '5-Pdfs']:
    os.makedirs(os.path.join(direcory, category), exist_ok=True)

#function to classify files
def classify_file(filename):
    #finding extension
    extension = '.' + filename.split('.')[-1]

    #choosing a category
    for category, extensions in categories.items():
        #checking if the extension is in the category to move file afterwards
        if extension in extensions:
            #constructing file path
            source_path = os.path.join(direcory, filename)
            dest_path = os.path.join(direcory, category, filename)

            os.rename(source_path, dest_path)
            print(f"Moved {filename} to {category}")
            break


#clasiifying current files in directory
for filename in os.listdir(direcory):
    classify_file(filename)


initial_files = os.listdir(direcory)


#does all the shinanigans
while True:

    time.sleep(5)
    current_files = os.listdir(direcory)

    new_files = os.listdir(set(current_files) - set(initial_files))

    for filename in new_files:
        classify_file(filename)

    initial_files = current_files
