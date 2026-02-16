from budget import Category
import pytest

def test_init_category():
    food = Category("Food")
    personal = Category("Personal")

    assert food.name == "Food"
    assert personal.name == "Personal"
    assert len(food.ledger) == 0
    assert len(personal.ledger) == 0

