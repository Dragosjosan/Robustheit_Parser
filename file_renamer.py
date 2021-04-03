import os
import argparse


def define_arguments():
    parser = argparse.ArgumentParser(description = "File Rename v.1.0")

    parser.add_argument('--original_name', help='Original file name', default='None')
    parser.add_argument('--new_name', help='NEw file name', default='None')

    args = parser.parse_args()

    original_name = args.original_name
    new_name = args.new_name
    return original_name, new_name


def get_cwd():
    """ gets the current working directory"""
    source_folder = os.getcwd()
    print(f'Current working directory: {source_folder}')
    return source_folder

def list_folders():
    original_name, new_name = define_arguments()
    folder = get_cwd()
    for dirname, dirs, files in os.walk(folder):
        for file in files:
            print(f"file: {file}")
            print(type(file))
            print(f"argument: {original_name}")
            print(type(original_name))
            if file == original_name:
                print('file is the same as argument')
                new_file = new_name
                os.rename(os.path.join(dirname, file), os.path.join(dirname, new_file))
            else:
                print("No match found")


list_folders()