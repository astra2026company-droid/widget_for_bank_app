def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    list_card_numbers_mask = []
    count_step = 0

    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр!")
    elif not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из цифр!")

    for i in range(len(card_number)):
        if count_step == 4:
            count_step = 0

            list_card_numbers_mask.append(" ")

        list_card_numbers_mask.append(card_number[i])

        count_step += 1

    for i in range(7, 14):
        if i == 9 or i == 14:
            continue

        list_card_numbers_mask[i] = "*"

    card_number = "".join(list_card_numbers_mask)
    return card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    if len(account_number) != 20:
        raise ValueError
    elif not account_number.isdigit():
        raise ValueError
    else:
        account_number = "**" + account_number[-4:]
        return account_number
