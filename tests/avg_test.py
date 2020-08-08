from main import avg_finder


def check_avg_finder():
    arr = [8, 9, 1]
    avg = 6
    return avg_finder(arr) == avg


def test_avg():
    print("Hello")
    assert check_avg_finder()
