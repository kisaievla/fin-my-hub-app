from __future__ import annotations

class Category:
    def __init__(self, name: str):
        self.name: str = name
        self.ledger: list[dict[str, object]] = []

    def deposit(self, amount: int | float, description: str = "") -> None:
        if not isinstance(amount, (int, float)):
            msg = f"amount must be int or float and not {type(amount)}"
            raise TypeError(msg)
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.ledger.append({"amount": amount, "description": description})

