import secrets, logging
from random import randint
from tinydb import TinyDB, Query

from src.models.game import Game

# from src.models.player import Player
import datetime
import secrets


class Round:
    """Round Class"""

    db_file = "./database/rounds.json"

    def __init__(
        self,
        tournament_id: str,
        round_name: str,
        round_id: str = None,  # token id for id in db (this not the Tournament id of round )
        game_list: list[tuple] = [],
        start_datetime: str | None = None,
        end_datetime: str = "",
    ) -> None:
        """Init method"""

        self.tournament_id = tournament_id
        self.round_id = round_id if round_id else secrets.token_hex(2)
        self.round_name = round_name if round_name else secrets.token_hex(2)
        self.game_list = game_list
        self.start_datetime = (
            start_datetime if start_datetime else str(datetime.datetime.now())[:18]
        )
        self.end_datetime = end_datetime

    @classmethod
    def table(cls):
        """Players db"""
        return TinyDB(cls.db_file, indent=4, separators=(",", ": "))

    def __repr__(self) -> str:
        """repr method"""
        return f"Round({self.__dict__})"

    def serialize(self):
        """Serialize player"""

        return self.__dict__

    def create(self):
        """Create round"""

        db = self.table()
        db.insert(self.serialize())
        logging.warning(f"player {self.round_id} créer")

    def delete(self):
        """delete a specific roudn"""

        db = self.table()
        query = Query()
        kwargs = {"round_id": self.round_id}
        db.remove(query.fragment(kwargs))
        logging.warning(f"Round {self.round_id} supprimé")

    def update(self, kwargs=None):
        """Update round"""

        if isinstance(kwargs, dict):
            for key, value in kwargs.items():
                setattr(self, key, value)
        self.delete()
        self.create()

    @classmethod
    def find(cls, round_id):
        """Find a round by id"""

        db = cls.table()
        query = Query()

        round_find = db.search(query.round_id == round_id)
        round_list = [Round(**dict(round)) for round in round_find]
        return round_list

    @classmethod
    def list_all(cls):
        """return list of dict with all entries"""

        round_list = cls.table().all()
        round_list = [Round(**dict(round)) for round in round_list]
        return round_list

    @classmethod
    def delete_all(cls):
        """delete all"""

        round_db = cls.table()
        logging.warning("la base a été supprimée")
        return round_db.truncate()

    def round_in_list(self):
        """Round info"""
        return [
            self.round_id,
            self.round_name,
            self.game_list,
            self.start_datetime,
            self.end_datetime,
        ]
