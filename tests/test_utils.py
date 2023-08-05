from utils.utils import split_card_name_and_account


def test_split_card_name_and_account():
    assert split_card_name_and_account("Visa Classic 6831982476737658") == ("Visa Classic", "6831982476737658")
    assert split_card_name_and_account("Счет 38976430693692818358") == ("Счет", "38976430693692818358")
