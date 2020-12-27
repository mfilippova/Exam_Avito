from unittest.mock import patch
from click.testing import CliRunner
import random
from pizza import Margherita, Pepperoni, Hawaiian
from decorators import bake, delivery, pickup
from cli import order, menu


def test_dict():
    assert Margherita().dict() == {
        "tomato_sauce": 200,
        "mozzarella": 100,
        "tomatoes": 100,
    }
    assert Pepperoni().dict() == {
        "tomato_sauce": 200,
        "mozzarella": 100,
        "pepperoni": 100,
    }
    assert Hawaiian().dict() == {
        "tomato_sauce": 200,
        "mozzarella": 100,
        "chicken": 100,
        "pineapples": 100,
    }


def test_eq():
    assert Margherita(size="L") == Margherita(size="L")
    assert Margherita(size="L") != Margherita(size="XL")
    assert Margherita() != Hawaiian()


def test_str():
    assert Margherita().__str__() == "- Margherita: " \
                    "tomato_sauce, mozzarella, tomatoes"


def test_bake():
    with patch.object(random, "randint", return_value=5):
        assert bake() == "Приготовили за 5с!"


def test_delivery():
    with patch.object(random, "randint", return_value=5):
        assert delivery() == "Доставили за 5с!"


def test_pickup():
    with patch.object(random, "randint", return_value=5):
        assert pickup() == "Забрали за 5с!"


def test_cli_delivery():
    with patch.object(random, "randint", return_value=5):
        runner = CliRunner()
        result = runner.invoke(order, ["Pepperoni", "--delivery"])
        assert result.output == "Приготовили за 5с!\nДоставили за 5с!\n"


def test_cli_pickup():
    with patch.object(random, "randint", return_value=5):
        runner = CliRunner()
        result = runner.invoke(order, ["Pepperoni"])
        assert result.output == "Приготовили за 5с!\nЗабрали за 5с!\n"


def test_menu():
    runner = CliRunner()
    result = runner.invoke(menu)
    assert (
        result.output == "- Margherita: tomato_sauce, mozzarella, tomatoes\n"
        "- Pepperoni: tomato_sauce, mozzarella, pepperoni\n"
        "- Hawaiian: tomato_sauce, mozzarella, chicken, pineapples\n"
    )
