import json
from confing import dir_path_json
from src.class_json import Operation


def open_json_file(dir_path=dir_path_json):
    with open(dir_path, encoding='UTF8') as f:
        operations_json = json.load(f)
        return operations_json


def format_secret_account(account):
    """Маскирует номер карты в формате XXXX XX** **** XXXX и счета в формате **XXXX"""
    if account:
        digits_from_account = ''.join(c for c in account if c.isdigit())
        letters_from_account = ''.join(c for c in account if c.isalpha())

        if "счет" in account.lower():
            formatted_account = digits_from_account[:-14]
            return letters_from_account + ' ' + f"**{formatted_account[2:]}"

        elif len(digits_from_account) == 16:
            formatted_account = " ".join([digits_from_account[i:i + 4] for i in range(0, 16, 4)])
            formatted_account = f"{formatted_account[:-12]}** **** {formatted_account[-4:]}"
            if letters_from_account:
                return letters_from_account + ' ' + formatted_account
            else:
                return formatted_account

        else:
            return account
    else:
        return ""


def sort_transactions(limit_operations, data_json=open_json_file()) -> list[Operation]:
    """Сортирует полученные данные из класса Operation по ключу state = "EXECUTED"
    а также производит сортировку даты по убыванию"""
    transaction_list = []
    for json_object in data_json:
        # Проверка на пустой объект
        if json_object:
            transaction = Operation(json_object)
            transaction_list.append(transaction)

    # Фильтрация транзакций с состоянием "EXECUTED"
    executed_transactions = [transaction for transaction in transaction_list if transaction.state == "EXECUTED"]

    # Сортировка списка транзакций по дате
    executed_transactions.sort(key=lambda x: x.date, reverse=True)
    return executed_transactions[:limit_operations]


def print_check(transactions) -> None:
    """Вывод на экран отсортированных данных в нужном представлении"""
    for transaction in transactions:
        indicator = ""
        if format_secret_account(transaction.from_account):
            indicator = " -> "

        print(f"{transaction.date.strftime('%d.%m.%Y')} {transaction.description}"
              f"\n{format_secret_account(transaction.from_account)}{indicator}"
              f"{format_secret_account(transaction.to_account)}"          
              f"\n{transaction.operation_amount['amount']} {transaction.operation_amount['currency']['name']}"
              f"\n")
