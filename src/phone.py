from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim <=0:
            raise ValueError(': Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return self.quantity + other.quantity
    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self,new):
        '''Проверяет новое значение на соотвествие (положительное,целое)'''
        if new <= 0 or not isinstance(new, int):
            raise ValueError(f'Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim=new
