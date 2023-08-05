import json


def load_operations(filename):
    """
    Загружает операции из файла
    """
    with open(filename, encoding='utf-8') as operations_file:
        data = json.load(operations_file)
    return data

