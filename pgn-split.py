from typing import TextIO
import chess.pgn
import io
def get_game(f: TextIO) -> str :
    '''
    reads lines of a file till it has generated an entire game
    '''
    starting_character : str = "["
    game : str = ""
    line : str = None
    while starting_character != "1":
        line = f.readline()
        try:
            starting_character = line[0]
        except:
            return "EOF"
    game += line
    end = False
    if "*" in line:
        end = True
    while not end:
        line = f.readline()
        game += line
        if "*" in line:
            end = True
    return game


def get_games(filepath: str):
    with open(filepath, 'r') as f:
        a = None
        while a != "EOF":
            a = get_game(f)
            game = chess.pgn.read_game(io.StringIO(a))
            

def parse_game(game : chess.pgn.Game):
    variations = 



def func (filepath: str):
    get_games(filepath=filepath)


func('lichess2.pgn')


