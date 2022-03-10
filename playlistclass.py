from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel
import ujson


class ExternalUrls(BaseModel):
    spotify: str


class Image(BaseModel):
    height: int
    url: str
    width: int


class ExternalUrls1(BaseModel):
    spotify: str


class Owner(BaseModel):
    display_name: str
    external_urls: ExternalUrls1
    href: str
    id: str
    type: str
    uri: str


class Tracks(BaseModel):
    href: str
    total: int


class Item(BaseModel):
    collaborative: bool
    description: str
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    owner: Owner
    primary_color: Any
    public: bool
    snapshot_id: str
    tracks: Tracks
    type: str
    uri: str


class PlaylistClass(BaseModel):
    href: str
    items: List[Item]
    limit: int
    next: str
    offset: int
    previous: Any
    total: int

    class Config:
        json_loads = ujson.loads
