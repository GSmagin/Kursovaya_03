from src.functions import sort_transactions
from src.functions import print_check


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
            "from": "1234567890123456",
            "to": "987654321098765"
        }
    ]
    assert print_check(sort_transactions(1, data)) == print()
