from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim <=0:
            raise ValueError(': Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return self.quantity + other.quantity
    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})" #"Phone('iPhone 14', 120000, 5, 2)"


m1=Item('Redmi',10,2)
m2=Phone('OnePlas',100,12,1)
#print(repr(m2))
print(m2+m2)
print(m1+m2)
print(isinstance(m1,Item))
#m2.number_of_sim = 0
print(m2.number_of_sim)