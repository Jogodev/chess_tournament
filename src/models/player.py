import logging
import json
import secrets
from tinydb import TinyDB, Query

PLAYERS_DATA_FILE = "./database/players.json"


class Player:
    """Player Class"""

    def __init__(
        self,
        last_name: str,
        first_name: str = "-",
        birthday: str = "-",
        sex: str = "-",
        elo: int = 0,
        player_id: str = "-",
    ):
        """init method"""

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

        # player id
        if player_id == "-":
            player_id = secrets.token_hex(4)
        self.player_id = player_id
        self.players_db = TinyDB("database/players.json")

    def __repr__(self):
        """repr method"""

        return f"Player({self.__dict__})"

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
        db.insert(self.serialize())

    def update(self):
        """Mise à jour du fichier json"""
        last_name = input("entrez le nom du joueur :")
        # TODO load db and all files
        # TODO Find the player in the Db loaded
        # TODO delete this player from db
        db = self.players_db
        db.all()
        for player in db:
            if player["last_name"] == last_name:
                db.update({"last_name": self.last_name}, doc_ids=[self.elo])
        # TODO create the 'new' player
        self.create()

    def delete(self):
        """delete a specific player"""
        last_name = input("entrez le nom du joueur que vous voulez supprimez")
        # TODO load db and all files
        # TODO Find the player in the Db loaded
        # TODO delete this player from db
        players_db = self.players_db
        players_db.all()
        for player in players_db:
            if player["last_name"] == last_name:
                players_db.remove(doc_ids=[1])

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
        # DEFAULT BEFORE CODING => RETURN EMPTY LIST
        return [players_db.all()]

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
