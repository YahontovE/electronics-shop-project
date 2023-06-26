import os.path
import os
import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all = []

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        '''Дает возможность обращаться к переменной name вне класса'''
        return self.__name

    @name.setter
    def name(self, new_name):
        '''Проверяет новое значение name на соответствие длине'''
        if len(new_name) > 10:
            raise Exception(f'Длина наименования товара превышает 10 символов.')
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        '''Берет данные из файла items.csv и делает из нах атрибуты класса '''
        try:
            with open(f'{os.path.dirname(os.path.realpath(__file__))}/items.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    if quantity == None:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    new = Item(name, price, quantity)
                    cls.all.append(new)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        return cls(name, price, quantity)

    @staticmethod
    def string_to_number(nam):
        '''Получает на вход строковое значение числа и переводит его в класс int'''
        nam = float(nam)
        nam = int(nam)
        return nam
