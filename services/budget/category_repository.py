from __future__ import annotations
from typing import Iterable, Protocol
from dataclasses import dataclass
from enum import Enum
from budget import Category

class CategoryCreateError(Enum):
    ALREADY_EXISTS = "already_exists"
    UNKNOWN = "unknown"

class CategoryGetError(Enum):
    DONT_EXIST = "Category doesn't exist"
    UNKNOWN = "unknown"
class CategoryUpdateError(Enum):
    DONT_EXIST = "Category doesn't exist"
    UPDATE_ERROR = "Error while updateing a record"
    UNKNOWN = "unknown"


@dataclass
class CategoryCreateResult:
    category: Category | None
    error: CategoryCreateError | None
@dataclass
class CategoryGetResult:
    category: Category | None
    error: CategoryGetError | None
@dataclass
class CategoryUpdateResult:
    category: Category | None
    error: CategoryUpdateError | None



class CategoryRepository(Protocol):
    def create_category(self, user_id: str, category: Category) -> CategoryCreateResult:
        ...
    def get_category(self, user_id: str, category_id: str) -> CategoryGetError:
        ...
    def list_categories(self, user_id: str) -> Iterable[Category]:
        ...
    def update_category(self, user_id: str, category_id: str, **kwargs) -> CategoryUpdateError:
        ...
    def delete_category(self, user_id: str, category_id: str) -> bool:
        ...
    def get_category_balance(self, user_id: str, category_id: str) -> float:
        ...



