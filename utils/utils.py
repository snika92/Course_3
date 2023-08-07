import json
from src.operation import Operation


def load_operations(filename):
    """
    Загружает операции из файла
    """
    with open(filename, encoding='utf-8') as operations_file:
        data = json.load(operations_file)
    return data


def split_card_name_and_account(card):
    """
    Разделяет строку на имя карты/счёта и её номер
    """
    card_account = card.split(" ")
    account = card_account.pop()
    card_name = " ".join(card_account)
    return card_name, account


def make_list_executed_operations(data):
    """
    Cоздает список выполненных операций
    """
    operations = []
    for item in data:
        if item:
            if item["state"] == "EXECUTED":
                op_id = item["id"]
                description = item["description"]
                summa = item["operationAmount"]["amount"]
                currency = item["operationAmount"]["currency"]["name"]
                date = item["date"].split("T")
                to_card_name, to_account = split_card_name_and_account(item["to"])
                if "from" in item:
                    from_card_name, from_account = split_card_name_and_account(item["from"])
                operation = Operation(op_id, description, summa, currency, date,
                                      to_card_name, to_account, from_card_name, from_account)
                operations.append(operation)
    return operations
