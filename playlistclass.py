from dataclasses import dataclass


@dataclass(init=True)
class PlaylistClass:
    name: str
    length: int

    def return_details(self):
        return self.name, self.length
