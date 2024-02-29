from src.class_json import Operation
import pytest
from datetime import datetime


def test_format_from_account_digits():
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
        "to": "9876543210987654"
    }

    transaction = Operation(data)
    formatted_account = transaction.format_from_account()

    assert formatted_account == "1234 56** **** 3456"


def test_format_from_account_alphanumeric():
    data = {
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
    }

    transaction = Operation(data)
    formatted_account = transaction.format_from_account()
    assert formatted_account == "a1b2c3d4e5f6g7h8"


# Добавьте другие тесты по необходимости

if __name__ == "__main__":
    pytest.main()
