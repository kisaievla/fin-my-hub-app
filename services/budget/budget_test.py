from budget import Category
import pytest


food = Category("Food")
personal = Category("Personal")

def test_init_category():
    assert food.name == "Food"
    assert personal.name == "Personal"
    assert len(food.ledger) == 0
    assert len(personal.ledger) == 0

def test_deposit():
    with pytest.raises(ValueError):
        food.deposit(-100, "negative amount")
    with pytest.raises(TypeError):
        personal.deposit("100")

    food.deposit(100, "Initial deposit")
    personal.deposit(1000)

    assert len(food.ledger) > 0
    assert len(personal.ledger) > 0
    assert food.ledger[0]["amount"] == 100
    assert food.ledger[0]["description"] == "Initial deposit"
    assert personal.ledger[0]["amount"] == 1000
    assert personal.ledger[0]["description"] == ""

