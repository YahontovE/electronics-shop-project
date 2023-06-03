"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

a1=Item('gvozdi',10,12)

def test_calculate_total_price():
    assert a1.calculate_total_price()==120

def test_apply_discount():
    assert a1.apply_discount()==11

def test_list_all():

    assert a1.all==a1.all
