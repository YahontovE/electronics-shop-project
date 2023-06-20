from src.item import Item


class Mixin:
    def __init____init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
            return self
        else:
            self.language = 'EN'
            return self


class Keyboard(Mixin, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def __str__(self):
        return f'{self.name}'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lg):
        if lg in ['EN', 'RU']:
            self.__language = lg
        else:
            raise AttributeError(f"property 'language' of 'KeyBoard' object has no setter")
