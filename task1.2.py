from typing import Tuple


def task(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> Tuple[bool, int]:
    intersect = min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and \
                min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4)
    if intersect:
        sx = sorted([x1, x2, x3, x4])
        sy = sorted([y1, y2, y3, y4])
        square = (sx[2] - sx[1]) * (sy[2] - sy[1])
    else:
        square = -1
    return intersect, square
