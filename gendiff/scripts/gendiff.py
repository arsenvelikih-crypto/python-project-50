import argparse

from gendiff.scripts import parsing_files
from gendiff.scripts.build_diff import build
from gendiff.scripts.formatters import formaters


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
    
    diff = build(file1, file2)
    formatter = formaters.get(format_name)
    if not formatter:
        raise ValueError(f'Unsupported format: {format_name}')
    return formatter(diff)


# основная функция
def main():

    args = parser_function()
    data1 = parsing_files.parse(args.first_file)
    data2 = parsing_files.parse(args.second_file)
    print(generate_diff(data1, data2))
        

if __name__ == '__main__':
    main()