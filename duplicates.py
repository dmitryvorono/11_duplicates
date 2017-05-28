import sys
import os
import pprint


def find_duplicates(path, saved_path_files={}, duplicates=[]):
    if not os.access(path, os.R_OK):
        return duplicates
    with os.scandir(path) as folder_iterator:
        for entry in folder_iterator:
            if entry.is_file():
                file_information = (entry.name, entry.stat().st_size)
                #print(file_information)
                if file_information in saved_path_files:
                    duplicates.append((saved_path_files[file_information], entry.path))
                else:
                    saved_path_files[file_information] = entry.path
            elif entry.is_dir():
                find_duplicates(entry.path, saved_path_files)
    return duplicates


def print_duplicates(duplicates):
    pprint.pprint(duplicates)


if __name__ == '__main__':
    duplicates = (find_duplicates('/home/dmitry'))
    print_duplicates(duplicates)
