from pathlib import Path

from gendiff.scripts import gendiff


def get_test_data_path(filename):

    return Path(__file__).parent / "test_data" / filename


def read_file(filename):

    return get_test_data_path(filename).read_text()


def test_gendiff():

    file1 = gendiff.parse_json(get_test_data_path("first.json"))
    file2 = gendiff.parse_json(get_test_data_path("second.json"))
    expected = read_file("expected.txt")
    actual = gendiff.generate_diff(file1, file2)
    assert actual == expected


