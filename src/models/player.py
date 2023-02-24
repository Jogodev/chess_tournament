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
            player_id: str = "",
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
        """Players db"""
        return TinyDB("database/players.json", indent=4, separators=(",", ": "))

    def __repr__(self):
        """repr method"""

        return f"Joueur {self.__dict__}"

    def serialize(self):
        """Serialize player"""

        return self.__dict__

    def create(self):
        """Create player"""

        db = self.table()
        db.insert(self.serialize())
        logging.info(f"Joueur {self.player_id} créer")

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

    @classmethod
    def boot(cls):
        """"""

        list_to_create = [
            ("AB12341", "Musk", "Elon", "h", 1),
            ("AB12342", "Lopez", "Jennifer", "f", 2),
            ("AB12343", "Ali", "Mohamed", "h", 3),
            ("AB12343", "Bertrand", "Alain", "h", 4),
            ("AB12344", "Vilar", "Jean", "h", 5),
            ("AB12345", "Doe", "John", "h", 6),
            ("AB12346", "Melenchon", "Jean-Luc", "h", 7),
            ("AB12347", "Birkin", "Jane", "f", 8),
        ]
        for player_id, last_name, first_name, gender, rank in list_to_create:
            player = Player(
                player_id=player_id,
                last_name=last_name,
                first_name=first_name,
                gender=gender,
                rank=int(rank),
            )
            player.create()
