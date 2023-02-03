import logging
import json
import secrets
from random import random

from tinydb import TinyDB, Query

PLAYERS_DATA_FILE = "./database/players.json"


class Player:
    """Player Class"""

    def __init__(
        self,
        player_id: int,
        last_name: str,
        first_name: str = "-",
        birthday: str = "-",
        sex: str = "-",
        elo: int = 0,
        rank: int = 0,
    ):
        """init method"""
        # player id
        self.player_id = player_id
        # last name
        self.last_name = last_name.upper()

        # first name
        self.first_name = first_name.capitalize()

        # birth day
        self.birthday = birthday

        # sex
        self.sex = sex

        # elo
        self.elo = elo

        self.rank = rank

        # database
        self.players_db = TinyDB(
            "database/players.json", sort_keys=True, indent=4, separators=(",", ": ")
        )

    def __repr__(self):
        """repr method"""

        return f"Player({self.__dict__})"

    @property
    def serialize(self):
        """Formatage d'un joueur"""

        return {
            "player_id": self.player_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "elo": self.elo,
        }

    def create(self):
        """Sauvegarde d'un joueur"""

        db = self.players_db
        db.insert(self.serialize)

    def update(self):
        """Mise à jour du fichier json"""
        # TODO load db and all files
        # TODO Find the player in the Db loaded
        # TODO delete this player from db
        # TODO create the 'new' player
        db = self.players_db
        db.all()
        db.update(self.serialize)
        self.create()

    def delete(self):
        """delete a specific player"""
        # TODO load db and all files
        # TODO Find the player in the Db loaded
        # TODO delete this player from db
        players_db = self.players_db
        players_db.all()
        players_db.remove(doc_ids=[self.player_id])

    @classmethod
    def find(self, key_value_dict: dict):
        """for a key_value_dict with {id : '12a'} find the palyer in the db and return an instace"""
        # TODO load db and all files
        # TODO Find the player in the Db loaded
        # TODO find in db where key_value_dict {id : '12a'} ==> find the good one
        players_db = TinyDB("database/players.json")

        # p_dict = {"firstname" : "alex", "lastname": "gaz"}
        # p = Player(**p_dict)

        # return p

    @classmethod
    def list_all(self) -> list:
        """return list of dict with all entries"""

        # TODO load DB
        # TODO transform in list of dict
        # TODO return the result
        players_db = TinyDB("database/players.json")
        # print(list(players_db.all()))
        players_db.all()
        player_list = []
        for player in players_db:
            player_list.append(player)
        return print(player_list)

    @classmethod
    def delete_all(self) -> None:
        """delete all"""
        # TODO load DB
        # drop everything
        players_db = TinyDB("database/players.json")
        return players_db.truncate()

    @classmethod
    def init_db(self):
        """boot db with vanessa"""

        p = Player(last_name="carlsen", elo=2890)
        p.create()
