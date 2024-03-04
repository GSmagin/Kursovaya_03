from src.functions import sort_transactions
from src.functions import print_check
from src.functions import format_secret_account


def test_sort_transactions():
    assert sort_transactions(1).__class__ == list


def test_print_check():
    data = [
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2022-01-01T12:00:00.000000",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Test Transaction",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655"
        }
    ]
    assert print_check(sort_transactions(1, data)) == print()


def test_format_secret_account():
    assert format_secret_account("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert format_secret_account("Счет 35158586384610753655") == "Счет **1585"
    assert format_secret_account("1596837868705199") == "1596 83** **** 5199"
    assert format_secret_account("15968378687051995464646") == "15968378687051995464646"
    assert format_secret_account("Visa Classic") == "Visa Classic"
    assert format_secret_account("") == ""


