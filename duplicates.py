import os
import pprint
import argparse
import collections


def categorize_files_by_name_and_size(path):
    saved_path_files = collections.defaultdict(list)
    folders = [path]
    for folder in folders:
        if not os.access(folder, os.R_OK):
            continue
        with os.scandir(folder) as folder_iterator:
            for entry in folder_iterator:
                if entry.is_file():
                    file_information = (entry.name, entry.stat().st_size)
                    saved_path_files[file_information].append(entry.path)
                elif entry.is_dir():
                    folders.append(entry.path)
    return saved_path_files


def find_duplicates(path):
    categorized_files = categorize_files_by_name_and_size(path)
    if categorized_files is None:
        return None
    return [categorized_files[key] for key in categorized_files
            if len(categorized_files[key]) > 1]


def print_duplicates(duplicates):
    pprint.pprint(duplicates)


def parse_commandline_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, nargs='?',
                        help='Path to target folder', default=os.getcwd())
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_commandline_arguments()
    duplicates = find_duplicates(args.path)
    print_duplicates(duplicates)
