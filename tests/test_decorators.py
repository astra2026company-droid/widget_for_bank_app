from src.decorators import log
import pytest


def test_log_in_console(capsys):
    """Функция, которая проверяет, что декоратор отрабатывает запись в консоль"""
    @log()
    def say_hi(name):
        return f"Hi, {name}"

    result = say_hi("Max")
    result_console = capsys.readouterr()
    assert result_console.out == f"Result working say_hi - Hi, Max\n"
    assert result == f"Hi, Max"


def test_log_in_file():
    @log("./data/logs.txt")
    def say_hi(name):
        return f"Hi, {name}"

    say_hi("Max")

    with open("./data/logs.txt", 'r', encoding="UTF-8") as file:
        result = file.read()

        assert result == "Result working say_hi - Hi, Max"


