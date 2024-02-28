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


    def format_from_account(self):
        if self.from_account:
            digits_from_account = ''.join(c for c in self.from_account if c.isdigit())
            letters_from_account = ''.join(c for c in self.from_account if c.isalpha())
            if len(digits_from_account) == 16:
                formatted_account = " ".join([digits_from_account[i:i + 4] for i in range(0, 16, 4)])
                formatted_account = f"{formatted_account[:-12]}** **** {formatted_account[-4:]}"
                return letters_from_account + ' ' + formatted_account
            elif len(digits_from_account) == 20:
                formatted_account = digits_from_account[:-16]
                formatted_account = f"**{formatted_account}"
                return formatted_account
            else:
                return self.from_account
        else:
            return f"Нет данных. Открытие вклада"
