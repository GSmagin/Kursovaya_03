from datetime import datetime


class Operation:
    """Работа с объектами в JSON-массиве.
            id = "id"
            state = "state
            operation_amount =  "amount"["operationAmount"]["amount"]
                                "currency"
                                    "name" ["operationAmount"]["currency"]["name"]
                                    "code" ["operationAmount"]["currency"]["code"]
            description = "description"
            from_account = "from"
            to_account = "to"
            """
    def __init__(self, data) -> None:
        self.id = data.get("id")
        self.state = data.get("state")
        self.date = datetime.strptime(data.get("date"), "%Y-%m-%dT%H:%M:%S.%f")
        self.operation_amount = {
            "amount": float(data["operationAmount"]["amount"]),
            "currency": {
                "name": data["operationAmount"]["currency"]["name"],
                "code": data["operationAmount"]["currency"]["code"]
            }
        }
        self.description = data.get("description")
        self.from_account = data.get("from")
        self.to_account = data.get("to")
