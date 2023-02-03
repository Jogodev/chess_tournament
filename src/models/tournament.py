import json
from tinydb import TinyDB
import secrets


class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        player_list: [],
        description="",
    ):
        self.id = secrets.token_hex(8)
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.id_current_round = -1
        self.round_list = []
        self.player_list = player_list
        self.description = description
        self.players_db = TinyDB("database/players.json")

    def serialize_tournament(self):
        """"""
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_round": self.id_current_round,
            "round_list": self.round_list,
            "player_list": self.player_list,
            "description": self.description,
        }

    def save_tournament(self):
        """"""

        db = self.players_db
        db.insert(self.serialize_tournament())

    def update_tournament(self):
        """"""
        pass

    def load_tournament(self):
        """"""


    def __repr__(self):
        return (
            f"Le tournoi n° {self.id} {self.name} viens de commencé à {self.location}"
        )

    def add_round(self):
        ronde = Ronde(player_list)
        self.ronde_list.append(ronde)
        self.id_current_round = id
