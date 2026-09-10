from widget import get_date
from datetime import datetime


def filter_by_state(list_dicts: list, key_value: str = 'EXECUTED') -> list:
    """Функция, которая сортирует список словарей по ключу"""
    sorted_list_dicts = []

    for collection in list_dicts:
        if collection["state"] == key_value:
            sorted_list_dicts.append(collection)

    return sorted_list_dicts


def sort_by_date(list_dicts: list, is_reverse: bool = True) -> list:
    """Функция, которая сортирует список по дате"""
    list_date_sorted = sorted(list_dicts, key=lambda dict_items: dict_items["date"], reverse=is_reverse)
    return list_date_sorted
