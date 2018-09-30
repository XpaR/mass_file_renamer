import random
import os
import argparse
import sys
import string

PERMITTED_EXTENSIONS=["jpg", "jpeg"]

TEMP_FOLDER_EXT = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))

START_INDEX = 30

# return true if extension allowed
def is_extension_allowed(str):
    for ext in PERMITTED_EXTENSIONS:
        if str.lower().endswith("." + ext.lower()):
            return True
    return False
    
# rename files with permitted extensions incrementally inside directory path_to_start
def rename_files(path_to_start):
    current_id = START_INDEX
    # keeping current_dir and folders variables for future use
    for current_dir,folders,files in os.walk(path_to_start):
        random.shuffle(files)
        for current_file in files:
            if is_extension_allowed(current_file):
                current_id += 1
                current_ext = current_file[current_file.rfind("."):]
                tmp_modified_name = str(current_id)+current_ext
                print(">>> {path}/{original} -> {modified}".format(path=path_to_start, original=current_file, modified=tmp_modified_name))
                os.rename(current_file, tmp_modified_name+TEMP_FOLDER_EXT)
                
    for current_dir,folders,files in os.walk(path_to_start):
        for current_file in files:
            if current_file[-len(TEMP_FOLDER_EXT):] == TEMP_FOLDER_EXT:
                os.rename(current_file, current_file[:-len(TEMP_FOLDER_EXT)])
    
                
    if current_id == START_INDEX:
        print("No files were found suitable to be renamed!")

        
def main():
    parser = argparse.ArgumentParser(description='Mass file renamer')
    parser.add_argument('--path', help='path of folder to modify files in')
    args = parser.parse_args()
    start_path = args.path # path to start looking at files from
    
    if start_path == None:
        print("Please supply parameter --path")
        sys.exit(1)
    
    rename_files(start_path)
    
    
if __name__ == "__main__":
    main()