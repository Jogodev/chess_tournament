from src.models.game import Game
from src.models.player import Player
import datetime


class Round:

    def __init__(
            self,
            round_id: int,
            round_name: str,
            game_list: list = [],
            start_datetime: str = datetime.datetime.now(),
            end_datetime: str = '',

    ):
        self.round_id = round_id
        self.round_name = round_name
        self.game_list = game_list
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def round_in_list(self):
        """Round info"""
        return [
            self.round_id,
            self.round_name,
            self.game_list,
            self.start_datetime,
            self.end_datetime
        ]

    def __repr__(self):
        return f"Match de la ronde n° {self.round_id}: "



