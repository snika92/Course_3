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


def test_repr(operation_instance):
    assert operation_instance.__repr__() == "Operation(441945886, Перевод организации, 31957.58, руб., " \
                                            "['2019-08-26', '10:50:58.294041'], Счет, 64686473678894779589, " \
                                            "Maestro, 1596837868705199)"


def test_format_date(operation_instance):
    assert operation_instance.format_date() == "26.08.2019"


def test_mask_from_account(operation_instance):
    assert operation_instance.mask_from_account() == "1596 83** **** 5199"


def test_mask_to_account(operation_instance):
    assert operation_instance.mask_to_account() == "**9589"
