from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel


class ExternalUrls(BaseModel):
    spotify: str


class Followers(BaseModel):
    href: Any
    total: int


class Image(BaseModel):
    height: Any
    url: str
    width: Any


class UserClass(BaseModel):
    display_name: str
    external_urls: ExternalUrls
    followers: Followers
    href: str
    id: str
    images: List[Image]
    type: str
    uri: str
