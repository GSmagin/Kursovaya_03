from class_json import Operation
from functions import operations_json

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

# Вывод данных для примера
for transaction in executed_transactions[:5]:
    print(f"ID: {transaction.id}")
    print(f"State: {transaction.state}")
    print(f"Date: {transaction.date}")
    print(f"Amount: {transaction.operation_amount['amount']} {transaction.operation_amount['currency']['code']}")
    print(f"Description: {transaction.description}")
    print(f"From: {transaction.from_account}")
    print(f"To: {transaction.to_account}")
    print("\n")
