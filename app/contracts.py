from pydantic import BaseModel


class Item(BaseModel):
    """Contract for item."""

    id: str
    age: int = None
    tags: list[str] = None
    created_at: str
    price: float
    item_description: str = None
