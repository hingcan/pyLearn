from collections import namedtuple
import pytest


fruit_w_kg = 2.35
vegetables_w_kg = 1.7


def test_range_food_weight():
    fr_weight = fruit_w_kg
    veg_weight = vegetables_w_kg
    range_kg = int(fr_weight + veg_weight) / 2

    assert range_kg <= 3


def test_vegetables_verification():
    fruit = ["apple", "banana", "mango", "lemon"]
    vegetables = ["potato", "carrot", "onion", "garlic"]

    assert "banana" in fruit
    assert "onion" in vegetables


def test_soup_check_ingrdts():
    vegetables = ["potato", "carrot", "onion", "garlic"]

    assert "potato" in vegetables and "carrot" in vegetables and "onion" in vegetables and "garlic" in vegetables


def test_namedtuple_immutable():
    MyTuple = namedtuple('MyTuple', ['key1', 'key2', 'key3'])
    my_tuple = MyTuple('value1', 'value2', 'value3')

    with pytest.raises(AttributeError):
        my_tuple.key2 = 'new_value'