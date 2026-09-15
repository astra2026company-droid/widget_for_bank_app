import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(fixture_generators, fixture_generators_answer_1, fixture_generators_answer_2):
    """Функция проверяет генератор filter_by_currency"""
    generator = filter_by_currency(fixture_generators)
    assert next(generator) == fixture_generators_answer_1
    assert next(generator) == fixture_generators_answer_2


def test_transaction_descriptions(
    fixture_generators, fixture_generators_description_1, fixture_generators_description_2
):
    """Функция, которая проверяет transaction_descriptions"""
    generator = transaction_descriptions(fixture_generators)
    assert next(generator) == fixture_generators_description_1
    assert next(generator) == fixture_generators_description_2


@pytest.mark.parametrize(
    "start, end, result",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        )
    ],
)
def test_card_number_generator_1(start, end, result):
    """Функция, проверяет card_number_generator в общем"""
    assert card_number_generator(start, end) == result


def test_card_number_generator_2():
    """Функция, которая проверяет генеративное выражение в card_number_generator"""
    generator_my_result = [
        "0000000000000001",
        "0000000000000002",
        "0000000000000003",
        "0000000000000004",
        "0000000000000005",
    ]
    generator_result = list(("0" * (16 - len(str(num))) + str(num) for num in range(1, 5 + 1)))
