import os
import argparse
import re


def define_arguments():
    parser = argparse.ArgumentParser(description="Robustheit Parser")

    parser.add_argument('--file', help='File to search for', default='compliance_probabilities.txt')

    args = parser.parse_args()

    file_name = args.file
    return file_name


def get_cwd():
    """ gets the current working directory"""
    source_folder = os.getcwd()
    print(f'Current working directory: {source_folder}')
    return source_folder


def list_folders():
    folder = get_cwd()
    robustheit_files = []
    for dirname, dirs, files in os.walk(folder):
        for file in files:
            if file == 'compliance_probabilities.txt':
                print(f"There is a match: {os.path.join(dirname, file)}")
                robustheit_files.append(os.path.join(dirname, file))
                print(f"The list: {robustheit_files}")
            else:
                pass
    return robustheit_files


def write_the_files():
    delete_csv_if_exists()
    files = list_folders()

    for file in files:
        with open('result_overview.txt', 'a', encoding='utf-8') as outfile, open(file, 'r', encoding='utf-8') as infile:
            for line in infile:
                if line.startswith('Nominal'):
                    print(f'This file will we writen into {outfile.name}: {line}')
                    new_line = re.sub("\s+", ",", line)
                    outfile.write(new_line + '\n')
                elif line[0].isdigit():
                    print(f'This file will we writen into {outfile.name}: {line}')
                    new_line = re.sub("\s+", ",", line)
                    outfile.write(new_line + '\n')
                elif line.startswith('-') and line[1].isdigit():
                    print(f'This file will we writen into {outfile.name}: {line}')
                    new_line = re.sub("\s+", ",", line)
                    outfile.write(new_line + '\n')
                else:
                    print(f'This line does not match your sorting algorithm: {line}')
        print(f'First draft of the list is: {outfile.name}')


def delete_csv_if_exists():
    for dirname, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file == 'result_overview.txt':
                try:
                    os.remove(file)
                    print(f'{file} was deleted')
                except OSError:
                    pass


if __name__ == '__main__':
    list_folders()
    write_the_files()
