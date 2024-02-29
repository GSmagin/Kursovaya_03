from confing import operations_json
from class_json import Operation


def sort_transactions(limit_operations=5) -> list[Operation]:
    """Сортирует полученные данные из класса Operation по ключу state = "EXECUTED"
    а также производит сортировку даты по убыванию"""
    transaction_list = []
    for json_object in operations_json:
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
        print(f"{transaction.date.strftime('%d.%m.%Y')} {transaction.description}"
              f"\n{transaction.format_from_account()} -> {transaction.format_to_account()}"
              f"\n{transaction.operation_amount['amount']} {transaction.operation_amount['currency']['code']}"
              f"\n")


