#This piece of code reformats the answers files by removing empty lines and changing the extension to .txt. Just a nice and easy way to clean up the files.

import os
from pathlib import Path

def remove_empty_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip():
                    file.write(line)
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def change_extension_to_txt(file_path):
    new_file_path = file_path.with_suffix('.txt')
    file_path.rename(new_file_path)
    return new_file_path

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            new_file_path = change_extension_to_txt(file_path)
            remove_empty_lines(new_file_path)

answers_directory = 'Awnsers'
process_directory(answers_directory)