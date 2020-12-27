import random


def log(message: str):
    """Параметрический декоратор, внешняя часть"""

    def wrapper(func):
        """Декоратор, принимающий функцию"""

        def inner(*args, **kwargs) -> str:
            """Внутренняя функция"""
            time = random.randint(0, 10)
            return message.format(time)

        return inner

    return wrapper


@log("Приготовили за {}с!")
def bake():
    """Готовит пиццу"""
    pass


@log("Доставили за {}с!")
def delivery():
    """Доставляет пиццу"""
    pass


@log("Забрали за {}с!")
def pickup():
    """Самовывоз"""
    pass
