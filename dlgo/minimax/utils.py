from dlgo.minimax.game_result import GameResult

__all__ = [
    'reverse_game_result',
]


def reverse_game_result(game_result):
    if game_result == GameResult.loss:
        return game_result.win
    if game_result == GameResult.win:
        return game_result.loss
    return GameResult.draw
