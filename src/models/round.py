from src.models.game import Game
from src.models.player import Player


class Round:

    def __init__(
            self,
            round_id: int,
            round_name: str,
            match_list: list = [],
            start_datetime: str = '',
            end_datetime: str = '',

    ):
        self.round_id = round_id
        self.round_name = round_name
        self.match_list = match_list
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def round_in_list(self):
        return [
            self.round_id,
            self.round_name,
            self.match_list,
            self.start_datetime,
            self.end_datetime
        ]

    def first_round(self, player_list):
        """Création des paires de la 1ere ronde"""
        pass

    def __repr__(self):
        return f"Match de la ronde n° {self.round_id}: "

    def game_tuple(self):
        """Match as tuple"""
        game = ([self.player_1["score"]], [self.player_2["score"]])
