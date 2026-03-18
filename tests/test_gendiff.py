from pathlib import Path

from gendiff.scripts import gendiff, parsing_files


# получение пути к тестовым данным
def get_test_data_path(filename):

    return Path(__file__).parent / "test_data" / filename


# Чтение тестовых данных
def read_file(filename):

    return get_test_data_path(filename).read_text()


# тестирование функции сравнения json файлов
def test_gendiff_json():

    file1 = parsing_files.parse(get_test_data_path("first.json"))
    file2 = parsing_files.parse(get_test_data_path("second.json"))
    expected = read_file("gendiff_expected.txt")
    actual = gendiff.generate_diff(file1, file2)
    assert actual == expected


# тестирование функции сравнения yaml файлов
def test_gendiff_yaml():

    file1 = parsing_files.parse(get_test_data_path("first.yaml"))
    file2 = parsing_files.parse(get_test_data_path("second.yaml"))
    expected = read_file("gendiff_expected.txt")
    actual = gendiff.generate_diff(file1, file2)
    assert actual == expected

