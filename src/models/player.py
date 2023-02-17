"""Player model"""
import secrets, logging
from tinydb import TinyDB, Query


class Player:
    """Player Class"""

    def __init__(
        self,
        last_name: str,
        first_name: str = "-",
        birthday: str = "-",
        gender: str = "-",
        rank: int = 0,
        score: float = 0.0,
        player_id: int = 0,
    ):
        self.player_id = player_id if player_id else secrets.token_hex(2)
        self.last_name = last_name.upper()
        self.first_name = first_name.capitalize()
        self.birthday = birthday
        self.gender = gender
        self.score = score
        self.rank = rank

    @classmethod
    def table(cls):
        """"""
        return TinyDB("database/players.json", indent=4, separators=(",", ": "))

    def __repr__(self):
        """repr method"""

        return f"Player({self.__dict__})"

    def serialize(self):
        """Serialize player"""

        return self.__dict__

    def create(self):
        """Create player"""

        db = self.table()
        db.insert(self.serialize())

    def update(self, kwargs=None):
        """Update player"""
        if isinstance(kwargs, dict):
            for key, value in kwargs.items():
                setattr(self, key, value)
        self.delete()
        self.create()

    def delete(self):
        """delete a specific player"""

        db = self.table()
        query = Query()
        kwargs = {"player_id": self.player_id}
        db.remove(query.fragment(kwargs))
        logging.warning(f"Joueur {self.player_id} supprimé")

    @classmethod
    def find(cls, player_id):
        """Find a player by id"""
        db = cls.table()
        db.all()
        query = Query()
        player_find = db.search(query.player_id == player_id)
        player_list = [Player(**dict(player)) for player in player_find]
        return player_list

    @classmethod
    def list_all(cls):
        """return list of dict with all entries"""

        players_db = cls.table()
        players_db.all()
        player_list = [player for player in players_db.all()]
        player_instance_list = [Player(**player) for player in player_list]
        return player_instance_list

    @classmethod
    def delete_all(cls):
        """delete all"""
        players_db = cls.table()
        return players_db.truncate()
