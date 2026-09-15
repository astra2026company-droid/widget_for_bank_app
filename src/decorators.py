from functools import wraps


def log(filename: str = "console") -> None:
    """Функция - декоратор, которая логирует выполнение функции в консоль либо в файл"""
    def log_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                result_working_func = f"{function.__name__} is finished the error - '{e}' with args - {args}, {kwargs}"
            else:
                result_working_func = f"Result working {function.__name__} - {result}"

            if filename == "console":
                print(result_working_func)
            else:
                with open(filename, 'w', encoding="UTF-8") as file:
                    file.write(result_working_func)
            return result

        return wrapper

    return log_decorator
