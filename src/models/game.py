# from models.player import Player


class Game:
    """ """

    def __init__(self, player_1, player_2):
        """ """
        self.player_1 = player_1
        self.player_2 = player_2

    def __repr__(self):
        return f"Match entre {self.player_1} et {self.player_2}"
