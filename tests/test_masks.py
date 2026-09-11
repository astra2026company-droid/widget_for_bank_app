import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_account, result_mask_account",
    [("64686473678894779589", "**9589"), ("35383033474447895560", "**5560"), ("73654108430135874305", "**4305")],
)
def test_get_mask_account(number_account, result_mask_account):
    """Функция, которая тестирует правильность маскировки номера счета"""
    assert get_mask_account(number_account) == result_mask_account


@pytest.mark.parametrize("number_account", ["3456", "21", "6468647367889477958923", "", "asdfghytrewiuytrgfty"])
def test_get_mask_account_length(number_account):
    """Функция, которая тестирует, что при неверном формате или длине, она выбрасывает исключение"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(number_account)


@pytest.mark.parametrize(
    "number_card, result_mask_card",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(number_card, result_mask_card):
    """Функция, которая проверяет правильность маскировки карты"""
    assert get_mask_card_number(number_card) == result_mask_card


@pytest.mark.parametrize(
    "number_card", ["15968378 68705199", "159683786870", "", "1596837868705199123", "asdfgtretgfddrty"]
)
def test_get_mask_card_number_length(number_card):
    """Функция, которая выбрасывает исключение, если карта не соответствует формату"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(number_card)
