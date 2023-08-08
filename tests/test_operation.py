from src.operation import Operation
import pytest


@pytest.fixture
def operation_instance():
    instance = Operation(441945886,
                         "Перевод организации",
                         "31957.58",
                         "руб.",
                         ["2019-08-26", "10:50:58.294041"],
                         "Счет",
                         "64686473678894779589",
                         "Maestro",
                         "1596837868705199")
    return instance


@pytest.fixture
def operation_instance_without_from():
    instance = Operation(441945886,
                          "Перевод организации",
                          "31957.58",
                          "руб.",
                          ["2019-08-26", "10:50:58.294041"],
                          "Счет",
                          "64686473678894779589")
    return instance


def test_repr(operation_instance):
    assert operation_instance.__repr__() == '26.08.2019 Перевод организации\n' \
                                            'Maestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n'


def test_format_date(operation_instance):
    assert operation_instance.format_date() == "26.08.2019"


def test_mask_from_account(operation_instance):
    assert operation_instance.mask_from_account() == "1596 83** **** 5199"


def test_mask_from_account_without_from(operation_instance_without_from):
    assert operation_instance_without_from.mask_from_account() == "Не указано"


def test_mask_to_account(operation_instance):
    assert operation_instance.mask_to_account() == "**9589"


def test_return_from_card_name(operation_instance):
    assert operation_instance.return_from_card_name() == "Maestro"


def test_return_from_card_name_without_card_name(operation_instance_without_from):
    assert operation_instance_without_from.return_from_card_name() == "Не указано"
