from typing import Iterable


def filter_by_currency(list_transactions: list, currency: str = "USD") -> Iterable:
    """Функция, которая поочередно выдает транзакции по заданной валюте"""
    for coll in list_transactions:
        if coll["operationAmount"]["currency"]["code"] == "USD":
            yield coll


def transaction_descriptions(list_trans: list) -> str:
    """Функция, которая возвращает описание каждой операции по очереди"""
    for coll in list_trans:
        yield coll["description"]


def card_number_generator(start: int = 1, stop: int = 9) -> str:
    """Функция, которая выдает номера карт в заданом диапазоне в формате 0000 0000 0000 0000"""
    generator_card_number = list(("0" * (16 - len(str(num))) + str(num) for num in range(start, stop + 1)))
    generator_card_number_new = []

    for card_number in generator_card_number:
        new_card_number = []
        count_step = 0

        for num in card_number:
            if count_step == 4:
                count_step = 0

                new_card_number.append(" ")

            new_card_number.append(num)

            count_step += 1

        new_card_number = "".join(new_card_number)
        generator_card_number_new.append(new_card_number)

    return generator_card_number_new
