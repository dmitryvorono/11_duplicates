import os
import pprint
import argparse


def find_duplicates(path, saved_path_files={}, duplicates=[]):
    if not os.access(path, os.R_OK):
        return duplicates
    with os.scandir(path) as folder_iterator:
        for entry in folder_iterator:
            if entry.is_file():
                file_information = (entry.name, entry.stat().st_size)
                if file_information in saved_path_files:
                    duplicates.append((saved_path_files[file_information],
                                       entry.path))
                else:
                    saved_path_files[file_information] = entry.path
            elif entry.is_dir():
                find_duplicates(entry.path, saved_path_files)
    return duplicates


def print_duplicates(duplicates):
    pprint.pprint(duplicates)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, nargs='?',
                        help='Path to target folder', default=os.getcwd())
    args = parser.parse_args()
    duplicates = find_duplicates(args.path)
    print_duplicates(duplicates)
