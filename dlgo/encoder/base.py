import importlib

__all__ = [
    'Encoder',
    'get_encoder_by_name',
]


class Encoder:
    def name(self):
        '''For logging and saving name of encoder.'''
        raise NotImplementedError()

    def encode(self, game_state):
        '''Turns Go board into numeric data.'''
        raise NotImplementedError()

    def encode_point(self, point):
        '''Turns Go board into an integer index.'''
        raise NotImplementedError()

    def decode_point_index(self, index):
        '''Turns an integer index back into a Go board point.'''
        raise NotImplementedError()

    def num_points(self):
        '''Number of point on the board.'''
        raise NotImplementedError()

    def shape(self):
        '''Shape of the encoded board.'''
        raise NotImplementedError()

def get_encoder_by_name(name, board_size):
    '''Create an encoder by its name'''
    if isinstance(board_size, int):
        # is square board
        board_size = (board_size, board_size)  
    module = importlib.import_module('dlgo.encoders.' + name)
    constructor = getattr(module, 'create') 
    return constructor(board_size)