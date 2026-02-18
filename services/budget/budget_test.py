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

def test_check_funds():
    with pytest.raises(ValueError):
        food.check_funds(-100)
    with pytest.raises(TypeError):
        personal.check_funds("100")

    assert food.check_funds(100) == True
    assert food.check_funds(1000) == False
    food.deposit(100, "second deposit")
    assert food.check_funds(200) == True

    assert personal.check_funds(100) == True
    assert personal.check_funds(1001) == False

def test_withdraw():
    test = Category("Test")
    with pytest.raises(ValueError):
        test.withdraw(-100)
    with pytest.raises(TypeError):
        test.withdraw("100")

    assert test.withdraw(0, "withdraw zero") == True
    test.deposit(100, "test deposit")
    assert test.withdraw(100, "test_withdraw") == True
    assert test.withdraw(10) == False

def test_transfer():
    a = Category("A")
    b = Category("B")

    with pytest.raises(TypeError):
        a.transfer("10", b)
        a.transfer(10, 2)

    with pytest.raises(ValueError):
        a.transfer(-10, b)

    a.deposit(10, "test deposit")
    assert a.transfer(10, b) == True and b.get_balance() == 10
    assert b.transfer(100, a) == False and b.get_balance() == 10
