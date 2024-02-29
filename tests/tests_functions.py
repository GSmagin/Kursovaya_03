from src.functions import sort_transactions
from src.functions import print_check


def test_sort_transactions():
    assert sort_transactions(1).__class__ == list


def test_print_check():
    assert print_check(sort_transactions(1)) == print(f"08.12.2019 Открытие вклада"
                                                      f"\nНет данных. Открытие вклада -> **90424"
                                                      f"\n41096.24 USD"
                                                      f"\n")
