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
    default_path = '.'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = default_path
    duplicates = find_duplicates(path)
    print_duplicates(duplicates)
