from src.phone import Phone,Item
import pytest

phone1=Phone('redmi',12000,15,2)
item1 = Item("Смартфон", 10000, 20)

def test__repr__():
    assert repr(phone1) == "Phone('redmi', 12000, 15, 2)"

def test__str__():
    assert str(phone1) == 'redmi'

def test_output_for_number_of_sim():
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim=0
        phone1.number_of_sim=1.5

def test__add__():
    assert item1 + phone1 == 35
    assert phone1 + phone1 == 30