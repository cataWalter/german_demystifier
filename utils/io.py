import re


def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as input_file:
        return re.sub(r'\n', '', input_file.read())


def write(file_path, result, write_enabled):
    if write_enabled:
        with open(file_path, "w", encoding="utf-8") as output_file:
            output_file.write(result)
    else:
        print(result)
