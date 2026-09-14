from typing import Iterable


def filter_by_currency(list_transactions: list, currency: str = "USD") -> Iterable:
    """Функция, которая поочередно выдает транзакции по заданной валюте"""
    for coll in list_transactions:
        if coll["operationAmount"]["currency"]["code"] == "USD":
            yield coll
