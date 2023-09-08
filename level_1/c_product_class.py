"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:

    def __init__(self, name: str, cost: float, description: str, weight: float):
        self.name = name
        self.description = description
        self.cost = cost
        self.weight = weight


if __name__ == '__main__':
    banana = Product(name='banana', description='An perfect bananas', cost=10.4, weight=1.0)
    print(f'Информация о продукте: {banana.name}, {banana.description}, {banana.cost}, {banana.weight}')
