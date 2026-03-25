from pathlib import Path

from gendiff.scripts import gendiff, parsing_files


# получение пути к тестовым данным
def get_test_data_path(filename):

    return Path(__file__).parent / "test_data" / filename


# Чтение тестовых данных
def read_file(filename):

    return get_test_data_path(filename).read_text()


# тестирование функции сравнения json файлов в формате stylish
def test_gendiff_json_stylish():

    file1 = parsing_files.parse(get_test_data_path("first.json"))
    file2 = parsing_files.parse(get_test_data_path("second.json"))
    file3 = parsing_files.parse(get_test_data_path("file1.json"))
    file4 = parsing_files.parse(get_test_data_path("file2.json"))
    expected = read_file("expected_stylish.txt")
    expected2 = read_file("expected_big_stylish.txt")
    actual = gendiff.generate_diff(file1, file2)
    actual2 = gendiff.generate_diff(file3, file4)

    assert actual == expected
    assert actual2 == expected2


# тестирование функции сравнения yaml файлов в формате stylish
def test_gendiff_yaml_stylish():

    file1 = parsing_files.parse(get_test_data_path("first.yaml"))
    file2 = parsing_files.parse(get_test_data_path("second.yaml"))
    file3 = parsing_files.parse(get_test_data_path("file1.yaml"))
    file4 = parsing_files.parse(get_test_data_path("file2.yaml"))
    expected = read_file("expected_stylish.txt")
    expected2 = read_file("expected_big_stylish.txt")
    actual = gendiff.generate_diff(file1, file2)
    actual2 = gendiff.generate_diff(file3, file4)

    assert actual == expected
    assert actual2 == expected2


# тестирование функции сравнения json файлов в формате plain
def test_gendiff_json_plain():

    file3 = parsing_files.parse(get_test_data_path("file1.yaml"))
    file4 = parsing_files.parse(get_test_data_path("file2.yaml"))
    expected = read_file("expected_plain.txt")
    actual = gendiff.generate_diff(file3, file4, 'plain')

    assert actual == expected


# тестирование функции сравнения yaml файлов в формате plain
def test_gendiff_yaml_plain():

    file3 = parsing_files.parse(get_test_data_path("file1.yaml"))
    file4 = parsing_files.parse(get_test_data_path("file2.yaml"))
    expected = read_file("expected_plain.txt")
    actual = gendiff.generate_diff(file3, file4, 'plain')

    assert actual == expected


