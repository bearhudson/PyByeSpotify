from dataclasses import dataclass
from datetime import datetime


@dataclass(init=True)
class TrackClass:
    name: str
    artist: list
    release: datetime
    is_single: bool = True
    album: str = ""

    def return_details(self):
        if self.is_single:
            return self.artist, self.name, self.album, self.release, self.is_single
        elif not self.is_single:
            return self.artist, self.name, self.release, self.is_single
