import enum

__all__ = [
    'GameResult',
]


class GameResult(enum.Enum):
    loss = 1
    draw = 2
    win = 3
