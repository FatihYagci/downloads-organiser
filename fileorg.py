import pathlib
import time
import os

#directory thats being used
direcory = "C:/Users/fatih/Downloads"

categories = {
    'Images': ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.bpg', 'svg'],
    'Videos': ['.webm', '.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg', '.3gp'],
    'Pdfs': ['.pdf'],
    'Documents': ['.txt', '.oxps', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods', '.odt', '.pwi', '.xsn', '.xps', '.dotx', '.docm', '.dox', '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt', 'pptx'],
}
for category in ['Images', 'Videos', 'Pdfs', 'Documents']:
    os.makedirs(os.path.join(direcory, category), exist_ok=True)

#function to classify files
def classify_file(filename):
    #finding extension
    extension = filename.split('.')[-1]

    #choosing a category
    for category, extensions in categories.items():
        #checking if the extension is in the category to move file afterwards
        if extension in extension:
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

    time.slee(5)
    current_files = os.listdir(direcory)

    new_files = os.listdir(set(current_files) - set(initial_files))

    for filename in new_files:
        classify_file(filename)

    initial_files = current_files