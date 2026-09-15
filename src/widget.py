from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция, которая обрабатывает счет или карту"""
    if len(type_and_number) < 10:
        raise ValueError("Вод не соответствует ожиданиям!")
    elif " " not in type_and_number:
        raise ValueError("Формат должен быть - Счет номер_счета или Название карты номер_карты!")

    list_type_and_number = type_and_number.split()
    payment_source = " ".join(list_type_and_number[:-1])
    numbers_source = list_type_and_number[-1]
    total_mask = payment_source + " "

    if payment_source.lower() == "счет" or payment_source.lower() == "счёт":
        total_mask += get_mask_account(numbers_source)
    else:
        total_mask += get_mask_card_number(numbers_source)

    return total_mask


def get_date(date: str) -> str:
    """Функция, которая форматирует дату"""
    if len(date) == 0:
        raise ValueError("Строка должна соответствовать формату 2024-03-11T02:26:18.671407 и не быть пустой!")
    if "T" not in date:
        raise ValueError("Строка несоответствует формату!")

    list_date = date.split("T")[0].split("-")
    list_date = list_date[::-1]

    if len(".".join(list_date)) != 10:
        raise ValueError("Дата не соответствует формату - 11.03.2025")

    return ".".join(list_date)
