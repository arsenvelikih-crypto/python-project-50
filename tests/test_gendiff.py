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
    file3 = parsing_files.parse(get_test_data_path("file1.json"))
    file4 = parsing_files.parse(get_test_data_path("file2.json"))
    expected = read_file("gendiff_expected.txt")
    expected2 = read_file("gendiff_big.txt")
    actual = gendiff.generate_diff(file1, file2)
    actual2 = gendiff.generate_diff(file3, file4)

    assert actual == expected
    assert actual2 == expected2


# тестирование функции сравнения yaml файлов
def test_gendiff_yaml():

    file1 = parsing_files.parse(get_test_data_path("first.yaml"))
    file2 = parsing_files.parse(get_test_data_path("second.yaml"))
    file3 = parsing_files.parse(get_test_data_path("file1.yaml"))
    file4 = parsing_files.parse(get_test_data_path("file2.yaml"))
    expected = read_file("gendiff_expected.txt")
    expected2 = read_file("gendiff_big.txt")
    actual = gendiff.generate_diff(file1, file2)
    actual2 = gendiff.generate_diff(file3, file4)

    assert actual == expected
    assert actual2 == expected2

