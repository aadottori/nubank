from info import users
import json
import formatter


def get_card_bills():
    card_bills = {}
    total = 0
    for user in users:
        with open(f"results/{user}/bills.json", 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            for bill in data:
                if bill["state"] == "open":
                    value = bill["summary"]["total_balance"]
                    card_bills[user] = formatter.number_to_currency(value)
                    total += value
                    break
    card_bills["total"] = formatter.number_to_currency(total)
    return card_bills

