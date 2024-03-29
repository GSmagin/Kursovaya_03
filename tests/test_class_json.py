import pytest
from src.class_json import Operation
from src.functions import format_secret_account


@pytest.fixture
def coll():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 987654321,
            "state": "EXECUTED",
            "date": "2022-01-01T12:00:00.000000",
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Another Test",
            "from": "a1b2c3d4e5f6g7h8",
            "to": "h8g7f6e5d4c3b2a1"
        },
        {
            "id": 987654321,
            "state": "EXECUTED",
            "date": "2022-01-01T12:00:00.000000",
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Another Test",
            "from": "",
            "to": ""
        }
    ]


def test_date():
    data = {
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
        "from": "1234567890123456",
        "to": "987654321098765"
    }
    transaction = Operation(data)
    formatted_account = transaction.date.strftime('%d.%m.%Y')

    assert formatted_account == "01.01.2022"


def test_format_secret_account_from_account(coll):
    coll_result = ["Maestro 1596 83** **** 5199",
                   "7158 30** **** 6758",
                   "Счет **1068",
                   "a1b2c3d4e5f6g7h8",
                   ""]
    i = 0
    for data_coll in coll:
        transaction = Operation(data_coll)
        formatted_account = format_secret_account(transaction.from_account)
        assert formatted_account == coll_result[i]
        i += 1


def test_format_secret_account_to_account(coll):
    coll_result = ["Счет **6864",
                   "Счет **3830",
                   "Счет **7766",
                   "h8g7f6e5d4c3b2a1",
                   ""]
    i = 0
    for data_coll in coll:
        transaction = Operation(data_coll)
        formatted_account = format_secret_account(transaction.to_account)
        assert formatted_account == coll_result[i]
        i += 1


if __name__ == "__main__":
    pytest.main()
