class Pizza:
    """Base pizza class"""

    def __init__(self, size: str = "L"):
        self.size = size
        self.tomato_sauce = 200
        self.mozzarella = 100

    def dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if k != "size"}

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__

    def __str__(self) -> str:
        return f'- {self.__class__.__name__}: {", ".join(self.dict().keys())}'


class Margherita(Pizza):
    """Margherita class"""

    def __init__(self, size: str = "L"):
        super().__init__(size)
        self.tomatoes = 100


class Pepperoni(Pizza):
    """Pepperoni class"""

    def __init__(self, size: str = "L"):
        super().__init__(size)
        self.pepperoni = 100


class Hawaiian(Pizza):
    """Hawaiian pizza class"""

    def __init__(self, size: str = "L"):
        super().__init__(size)
        self.chicken = 100
        self.pineapples = 100
