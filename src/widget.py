from src.masks import get_mask_card_number, get_mask_account


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
