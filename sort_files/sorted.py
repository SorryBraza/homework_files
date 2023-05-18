def create_file_data(file_name):
    with open(file_name, 'rt') as file:
        file_data = {}
        file_text = []
        name = file_name.replace("sort_files/", "")
        q = len(file.readlines())
        for i in range(1, q + 1):
            file_text += [f'Строка номер {i} файла номер {name.replace(".txt", "")}']
        file_data['name'] = name
        file_data['quantity'] = q
        file_data['text'] = file_text
    return file_data

files_data = [create_file_data('sort_files/1.txt'), create_file_data('sort_files/2.txt'), create_file_data('sort_files/3.txt')]
files_data.sort(key=lambda d: d['quantity'])

with open('sort_files/sorted_files.txt', 'w') as f:
    for file in files_data:
        f.write(f'{file["name"]}\n')
        f.write(f'{str(file["quantity"])}\n')
        for line in file["text"]:
            f.write(f'{line}\n')

