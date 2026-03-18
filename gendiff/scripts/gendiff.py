import argparse

from gendiff.scripts import parsing_files


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
def generate_diff(file1, file2):

    diff = []
    keys = sorted(file1.keys() | file2.keys())

    for key in keys:
        if key not in file2:
            diff.append(f"  - {key}: {file1[key]}")
        elif key not in file1:
            diff.append(f"  + {key}: {file2[key]}")
        elif file1[key] != file2[key]:
            diff.append(f"  - {key}: {file1[key]}")
            diff.append(f"  + {key}: {file2[key]}")      
        else:
            diff.append(f"  {key}: {file1[key]}")   
    return "{\n" + "\n".join(diff) + "\n}"
        

# основная функция
def main():

    args = parser_function()
    data1 = parsing_files.parse(args.first_file)
    data2 = parsing_files.parse(args.second_file)
    print(generate_diff(data1, data2))
        

if __name__ == '__main__':
    main()