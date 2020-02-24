import random

from dlgo.minimax.game_result import GameResult
from dlgo.minimax.utils import reverse_game_result
from dlgo.agent import Agent

__all__ = [
    'MinimaxAgent',
]


def best_result(game_state):
    '''Find the best result for next_player given this game state.
    Returns:
        GameResult.win if next_player can guarantee a win
        GameResult.draw if next_player can guarantee a draw
        GameResult.loss if, no matter what next_player chooses, the
            opponent can still force a win
    '''
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return GameResult.win
        elif game_state.winner() is None:
            return GameResult.draw
        else:
            return GameResult.loss

    best_result_so_far = GameResult.loss
    opponent = game_state.next_player.other
    for candidate_move in game_state.legal_moves():
        # See what the board would look like if we play this move.
        next_state = game_state.apply_move(candidate_move)
        # Find out our opponent's best move.
        opponent_best_result = best_result(next_state)
        # Whatever our opponent wants, we want the opposite.
        our_result = reverse_game_result(opponent_best_result)
        # See if this result is better than the best we've seen so far.
        if our_result.value > best_result_so_far.value:
            best_result_so_far = our_result
    return best_result_so_far


class MinimaxAgent(Agent):
    def select_move(self, game_state):
        winning_moves = []
        draw_moves = []
        losing_moves = []

        for possible_move in game_state.legal_moves():
            next_state = game_state.apply_move(possible_move)
            # Figure out their best possible outcome from there.
            opponent_best_outcome = best_result(next_state)
            # Our outcome is the opposite of our opponent's outcome.
            our_best_outcome = reverse_game_result(opponent_best_outcome)

            if our_best_outcome == GameResult.win:
                winning_moves.append(possible_move)
            elif our_best_outcome == GameResult.draw:
                draw_moves.append(possible_move)
            else:
                losing_moves.append(possible_move)

        if winning_moves:
            return random.choice(winning_moves)
        if draw_moves:
            return random.choice(draw_moves)
        return random.choice(losing_moves)
