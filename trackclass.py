from dataclasses import dataclass
from datetime import datetime


@dataclass(init=True)
class TrackClass:
    name: str
    artist: list
    album: str
    release: datetime
    is_single: bool = True

    def return_details(self):
        return self.name, self.artist, self.release, self.is_single
