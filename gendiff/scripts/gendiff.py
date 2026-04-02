import argparse

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.scripts import parsing_files
from gendiff.scripts.build_diff import build

# словарь с форматами вывода
formaters = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json
}


# парсер командной строки
def parser_function():

    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
        )
    parser._action_groups[1].title = "options:"
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        '-f', '--format', 
        help='set format of output',
        default='stylish',
        type=str
    )
    return parser.parse_args()


# Сравнение двух файлов
def generate_diff(file1, file2, format_name='stylish'):
    if isinstance(file1, str):
        data1 = parsing_files.parse(file1)
    else:
        data1 = file1

    if isinstance(file2, str):
        data2 = parsing_files.parse(file2)
    else:
        data2 = file2

    diff = build(data1, data2)
    formatter = formaters.get(format_name)
    if not formatter:
        raise ValueError(f'Unsupported format: {format_name}')
    return formatter(diff)


# основная функция
def main():

    args = parser_function()
    data1 = parsing_files.parse(args.first_file)
    data2 = parsing_files.parse(args.second_file)
    print(generate_diff(data1, data2, args.format))
        

if __name__ == '__main__':
    main()