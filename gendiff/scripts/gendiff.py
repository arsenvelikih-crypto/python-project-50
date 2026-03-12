import argparse
def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
        )
    parser._action_groups[1].title = "options:"
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        '-f', 
        '--format', 
        metavar='FORMAT',
        help='set format of output'
    )

    args = parser.parse_args()

    print(args.first_file)
    print(args.second_file)




if __name__ == '__main__':
    main()