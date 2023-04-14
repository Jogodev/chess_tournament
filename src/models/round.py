"""Class Round"""
import logging
import secrets

from tinydb import TinyDB, Query

from helpers.time import get_datetime


class Round:
    """Round Class"""

    db_file = "./database/rounds.json"

    def __init__(
            self,
            tournament_id: str,
            round_name: str,
            game_list: list,
            round_id: str = None,  # token id for id in db (this not the Tournament id of round )
            start_datetime: str | None = None,
            end_datetime: str = "",
    ) -> None:
        """Init method"""

        self.tournament_id = tournament_id
        self.round_name = round_name if round_name else secrets.token_hex(2)
        self.round_id = round_id if round_id else secrets.token_hex(2)
        self.game_list = game_list
        self.start_datetime = start_datetime if start_datetime else get_datetime()
        self.end_datetime = end_datetime

    @classmethod
    def table(cls):
        """Players db"""

        # fn = "./database/rounds.json"
        return TinyDB(Round.db_file, indent=4, separators=(",", ": "))

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
        print(f"Ronde {self.round_id} créer")

    def delete(self):
        """delete a specific round"""

        db = self.table()
        query = Query()
        kwargs = {"round_id": self.round_id}
        db.remove(query.fragment(kwargs))
        print(f"Round {self.round_id} supprimé")

    def update(self):
        """Update round"""

        db = self.table()
        query = Query()
        db.update({"game_list": self.game_list}, query.round_id == self.round_id)
        db.update({"end_datetime": self.end_datetime}, query.round_id == self.round_id)

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
        print("la base des rondes a été supprimée")
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


