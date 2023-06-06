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
        self.__name=name
        self.price=price
        self.quantity=quantity
        self.all.append(self)


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
        self.price=self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        if len(self.__name)<=10:
            return self.__name
        return f'Длина наименования товара превышает 10 символов.'

m1=Item('СуперРучкаы',3000,5)

print(m1.name)

