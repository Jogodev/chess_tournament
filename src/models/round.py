from src.models.game import Game
import itertools


class Round:

    def __init__(
            self,
            round_id: int,
            round_name: str,
            match_list: list,
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

    def pairring_player(self, player_list):
        """Création des paires de la 1ere ronde"""
        results_of_pairring = itertools.combinations(list(player_list), 2)
        return results_of_pairring

    def __repr__(self):
        return f"Match de la ronde n° {self.round_id}: "
