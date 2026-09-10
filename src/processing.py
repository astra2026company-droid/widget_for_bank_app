def filter_by_state(list_dicts: list, key_value: str = 'EXECUTED') -> list:
    """Функция, которая сортирует список словарей по ключу"""
    sorted_list_dicts = []

    for collection in list_dicts:
        if collection["state"] == key_value:
            sorted_list_dicts.append(collection)

    return sorted_list_dicts
