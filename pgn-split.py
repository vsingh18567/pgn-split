from typing import TextIO
from chess import pgn, Move
import io
import copy
import os


class PgnSplitter:
    
    def __init__(self, filepath):
        self.counter = 0
        self.filepath = filepath
        self.get_games(filepath)

    def get_game(self, f: TextIO) -> str :
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
            if f.readline() == "":
                return "EOF"
            game += line
            if "*" in line:
                end = True
        return game


    def get_games(self, filepath: str):
        with open(filepath, 'r') as f:
            a = None
            while a != "EOF":
                a = self.get_game(f)
                game = pgn.read_game(io.StringIO(a))
                self.parse_game(game)



    def parse_game(self, game: pgn.GameNode):
        vars = game.variations
        if game.next() == None:
            self.remove_variations(game.game())
            self.write_game(str(game.game()))
        elif len(vars) == 1:
            self.parse_game(game.next())
        else:
            for i in range(len(vars)):
                new_game = copy.deepcopy(game)
                new_game.promote_to_main(new_game.variations[i])
                self.parse_game(new_game.next())

    def remove_variations(self, game: pgn.GameNode):
            vars = game.variations
            if len(vars) == 0:
                self.write_game(str(game.game()))
            elif len(vars) == 1:
                self.remove_variations(game.next())
            else:
                for var in vars[1:]:
                    game.remove_variation(var)
                self.remove_variations(game.next())            
        

    def write_game(self, string):
        filepath = f"pgns/game{self.counter}.pgn"
        if not os.path.isdir("./pgns"):
            os.mkdir("pgns")
        elif os.path.isfile(filepath):
                os.remove(filepath)
        with open (filepath, "w") as f:
            f.write(string)
        
        print(f"PGN {self.counter} created")
        self.counter += 1


PgnSplitter('gotham.pgn')


