import enum
import random

from dlgo.minimax.game_result import GameResult
from dlgo.minimax.utils import reverse_game_result
from dlgo.agent import Agent

__all__ = [
    'DepthPrunedAgent',
]

MAX_SCORE = 999999
MIN_SCORE = -999999


def best_result(game_state, max_depth, eval_fn):
    '''Find the best result for next_player given this game state.'''
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return MAX_SCORE
        else:
            return MIN_SCORE

    # If maximum search depth reached, use heuristic to
    # decide how good this sequence is.
    if max_depth == 0:
        return eval_fn(game_state)

    best_so_far = MIN_SCORE
    for candidate_move in game_state.legal_moves():
        # See what the board would look like if we play this move.
        next_state = game_state.apply_move(candidate_move)
        # Find out our opponent's best move.
        opponent_best_result = best_result(next_state, max_depth - 1, eval_fn)
        # Whatever our opponent wants, we want the opposite.
        our_result = -1 * opponent_best_result
        # See if this result is better than the best we've seen so far.
        if our_result > best_so_far:
            best_so_far = our_result

    return best_so_far


class DepthPrunedAgent(Agent):
    def __init__(self, max_depth, eval_fn):
        self.max_depth = max_depth
        self.eval_fn = eval_fn

    def select_move(self, game_state):
        best_moves = []
        best_score = None

        for possible_move in game_state.legal_moves():
            # Calculate the game state if we select this move.
            next_state = game_state.apply_move(possible_move)
            # Find out our opponent's best move.
            opponent_best_outcome = best_result(
                next_state, self.max_depth, self.eval_fn)
            # Our outcome is the opposite of our opponent's outcome.
            our_best_outcome = -1 * opponent_best_outcome
            if (not best_moves) or our_best_outcome > best_score:
                # This is the best move so far.
                best_moves = [possible_move]
                best_score = our_best_outcome
            elif our_best_outcome == best_score:
                # This is as good as our previous best move.
                best_moves.append(possible_move)

        # For variety, randomly select among all equally good moves.
        return random.choice(best_moves)
