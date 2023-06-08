"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

a1=Item('gvozdi',10,12)

def test_calculate_total_price():
    assert a1.calculate_total_price()==120

def test_apply_discount():
    assert a1.apply_discount()==11

def test_list_all():

    assert a1.all==a1.all

def test_name():
    a1.name = 'Смартфон'
    assert a1.name == 'Смартфон'

def test_name_assert():
    a1.name = 'Супертелефон'
    assert a1.name=='gvozdi'
    a1.name = 'Supergvozdi'
    assert a1.name == 'gvozdi'

def test_instantiate_from_csv():
     Item.instantiate_from_csv()  # создание объектов из данных файла
     assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5