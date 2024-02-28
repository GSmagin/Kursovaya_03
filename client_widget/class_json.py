from datetime import datetime


class Operation:
    def __init__(self, data):
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
