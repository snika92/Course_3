from utils.utils import load_operations
from utils.utils import split_card_name_and_account
from utils.utils import make_list_executed_operations


def test_load_operations():
    filename = "./tests/test_json.json"
    assert load_operations(filename) == [{
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def test_split_card_name_and_account():
    assert split_card_name_and_account("Visa Classic 6831982476737658") == ("Visa Classic", "6831982476737658")
    assert split_card_name_and_account("Счет 38976430693692818358") == ("Счет", "38976430693692818358")


def test_make_list_executed_operations():
    data = [{
        "id": 594226727,
        "state": "CANCELLED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    result = [x.__dict__ for x in make_list_executed_operations(data)]
    assert result == [{'op_id': 863064926, 'description': 'Открытие вклада', 'summa': '41096.24', 'currency': 'USD', 'date': ['2019-12-08', '22:46:21.935582'], 'to_card_name': 'Счет', 'to_account': '90424923579946435907', 'from_card_name': None, 'from_account': None}, {'op_id': 441945886, 'description': 'Перевод организации', 'summa': '31957.58', 'currency': 'руб.', 'date': ['2019-08-26', '10:50:58.294041'], 'to_card_name': 'Счет', 'to_account': '64686473678894779589', 'from_card_name': 'Maestro', 'from_account': '1596837868705199'}]
