from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция, которая обрабатывает счет или карту"""
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
    list_date = date.split("T")[0].split("-")
    list_date = list_date[::-1]

    return ".".join(list_date)
