import click
from pizza import Margherita, Pepperoni, Hawaiian
import decorators as d


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if delivery:
        print(d.bake())
        print(d.delivery())
    else:
        print(d.bake())
        print(d.pickup())


@cli.command()
def menu():
    """Выводит меню"""
    print(Margherita().__str__())
    print(Pepperoni().__str__())
    print(Hawaiian().__str__())


if __name__ == "__main__":
    cli()
