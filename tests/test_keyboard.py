from src.keyboard import Keyboard
import pytest

kb = Keyboard('Dark Project KD87A', 9600, 5)
def test__str__():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"

def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == "RU"
    #Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

def test_override_lang():
    with pytest.raises(AttributeError):
        kb.language = 'CH'