from typing import Optional, Any

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    image: str
    description: str
    price: int
    sellerId: int
    sellerName: str

    @classmethod
    def from_tuple(cls, tpl: tuple):
        return cls(**{k: v for k, v in zip(cls.__fields__.keys(), tpl)})


class Seller(BaseModel):
    id: int
    name: str
    description: str
    profileImage: Optional[str]
    banner: Optional[str]

    @classmethod
    def from_tuple(cls, tpl: tuple):
        return cls(**{k: v for k, v in zip(cls.__fields__.keys(), tpl)})


class Response(BaseModel):
    data: Optional[Any]
    error: Optional[dict]
