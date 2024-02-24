import os
import hashlib
import shutil

def process_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        hashed_data = hashlib.md5(data).hexdigest()
        mapped_data = {i: ord(char) for i, char in enumerate(hashed_data[:1024])}
        return mapped_data

def traverse_and_process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            mapped_data = process_file(file_path)

            output_file_path = os.path.join(output_folder, file_name + '_mapped.txt')
            with open(output_file_path, 'w') as output_file:
                output_file.write('mapped_data = {\n')
                for key, value in mapped_data.items():
                    output_file.write(f'    {key}: {value},\n')
                output_file.write('}\n')

if __name__ == "__main__":
    input_folder = ''
    output_folder = ''
    traverse_and_process_folder(input_folder, output_folder)
