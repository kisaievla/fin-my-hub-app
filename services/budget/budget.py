from __future__ import annotations

class Category:
    def __init__(self, name: str):
        self.name: str = name
        self.ledger: list[dict[str, object]] = []

    def deposit(self, amount: int | float, description: str = "") -> None:
        """
        Add a deposit to the ledger.
        """
        if not isinstance(amount, (int, float)):
            msg = f"amount must be int or float and not {type(amount)}"
            raise TypeError(msg)
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self) -> float:
        """
        Calculate and return the current balance.
        """
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount: int | float) -> bool:
        """
        Check if enough funds exist for the given amount.
        Return True if sufficient, otherwise False.
        """
        if not isinstance(amount, (int, float)):
            msg = f"amount must be int or float and not {type(amount)}"
            raise TypeError(msg)
        if amount < 0:
            raise ValueError("amount must be non-negative")
        return amount <= self.get_balance()

    def withdraw(self, amount: int | float, description: str = "") -> bool:
        """
        Add a withdrawal (as a negative amount) if funds are sufficient.
        Return True if successful, otherwise False.
        """
        if not isinstance(amount, (int, float)):
            msg = f"amount must be int or float and not {type(amount)}"
            raise TypeError(msg)
        if amount < 0:
            raise ValueError("amount must be non-negative")
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def transfer(self, amount: int | float, other_category: "Category") -> bool:
        """
        Transfer amount to another Category.
        Record a withdrawal in this category and
        a deposit in the other category if funds are sufficient.
        Return True if successful, otherwise False.
        """
        if not isinstance(amount, (int, float)):
            msg = f"amount must be int or float and not {type(amount)}"
            raise TypeError(msg)
        if amount < 0:
            raise ValueError("amount must be non-negative")
        if not isinstance(other_category, Category):
            msg = f"amount must be Category and not {type(other_category)}"
            raise TypeError(msg)
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {other_category.name}")
        other_category.deposit(amount, f"Transfer from {self.name}")
        return True

