from dataclasses import dataclass


@dataclass
class Point2D:
    x: int
    y: int

    def __iter__(self):
        return (self.x, self.y).__iter__()
