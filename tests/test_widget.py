import pytest
from librt.vecs import append

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("type_and_number, result",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Счет 64686473678894779589", "Счет **9589"),
                          ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                          ("Счет 35383033474447895560", "Счет **5560"),
                          ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                          ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                          ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                          ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(type_and_number, result):
    """Функция, проверяет, что конкретно распознается и проверяется тип данных карта или счет"""
    assert mask_account_card(type_and_number) == result


@pytest.mark.parametrize("type_and_number",
                         ["64686473678894779589", "Maestro", "", "Счет 646864736788947795",
                          "Visa 683198247673765843"])
def test_mask_account_card_length(type_and_number):
    """Функция, которая проверяет выбрасывается ли ошибка при некорректных данных"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(type_and_number)


def test_get_date(fixture_get_date):
    """Функция, проверяет правильность форматирования даты"""
    assert get_date(fixture_get_date) == "11.03.2024"


@pytest.mark.parametrize("date", [" ", "", "2024-03-102:26:18.671407", "2024-0-11T02:26:18.671407"])
def test_get_date_exception(date):
    """Функция, которая проверяет, что при неверном формате выбрасывается исключение"""
    with pytest.raises(ValueError) as exc_info:
        get_date(date)
