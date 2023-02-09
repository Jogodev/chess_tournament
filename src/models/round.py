
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


# round_1 = Round(1, "1ere ronde")
#round_1.first_round([{"last_name": "Alain, "rank": 1, "score": 0.0}, {"last_name": "Stan", "rank": 2, "score": 0.0}, {"last_name": "David", "rank": 3, "score": 0.0}, {"last_name": "Scott", "rank": 4, "score": 0.0}, {"last_name": "Kevin", "rank": 5, "score": 0.0}, {"last_name": "Lucie", "rank": 6, "score": 0.0}, {"last_name": "Elodie", "rank": 7, "score": 0.0}, {"Julie", "rank": 8, "score": 0.0}])
# print(round_1.first_round(["Alain", "Stan", "David", "Scott", "Kevin", "Lucie", "Elodie", "Julie"]))