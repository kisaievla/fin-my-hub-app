from __future__ import annotations
from typing import Protocol
from budget import Category

class CategoryRepository(Protocol):
    def create_category(self, user_id: str, category: Category) -> Category: ...
