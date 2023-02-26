"""Player model"""
import secrets, logging
from random import randint
from tinydb import TinyDB, Query


class Player:
    """Player Class"""

    def __init__(
            self,
            last_name: str,
            first_name: str = "-",
            birthday: str = "-",
            gender: str = "-",
            elo: int = 0,
            score: float = 0.0,
            player_id: str = "",
            select_id: int = randint(0, 30),
    ):
        self.player_id = player_id if player_id else secrets.token_hex(2)
        self.select_id = select_id
        self.last_name = last_name.upper()
        self.first_name = first_name.capitalize()
        self.birthday = birthday
        self.gender = gender
        self.score = score
        self.elo = elo

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
    def find_by_select_id(cls, select_id):
        """Find a player by select_id"""
        db = cls.table()
        db.all()
        query = Query()
        player_find = db.search(query.select_id == select_id)
        player_list = [Player(**dict(player)) for player in player_find]
        return player_list

    @classmethod
    def list_all(cls):
        """return list of dict with all entries"""

        players_db = cls.table()
        players_db.all()
        player_list = [player for player in players_db.all()]
        player_instance_list = [player for player in player_list]
        return player_instance_list

    @classmethod
    def delete_all(cls):
        """delete all"""
        players_db = cls.table()
        logging.warning("la base a été supprimée")
        return players_db.truncate()


    @classmethod
    def boot(cls):
        """"""

        list_to_create = [
            (1, "AB12341", "Musk", "Elon", "01/01/1988", "h", randint(0, 50)),
            (2, "AB12342", "Lopez", "Jennifer", "01/01/1988", "f", randint(0, 50)),
            (3, "AB12344", "Ali", "Mohamed", "01/01/1988", "h", randint(0, 50)),
            (4, "AB12345", "Bertrand", "Alain", "01/01/1988", "h", randint(0, 50)),
            (5, "AB12346", "Vilar", "Jean", "01/01/1988", "h", randint(0, 50)),
            (6, "AB12347", "Doe", "John", "01/01/1988", "h", randint(0, 50)),
            (7, "AB12348", "Melenchon", "Jean-Luc", "01/01/1988", "h", randint(0, 50)),
            (8, "AB12349", "Birkin", "Jane", "01/01/1988", "f", randint(0, 50)),
        ]
        for select_id, player_id, last_name, first_name, birthday, gender, elo in list_to_create:
            player = Player(
                select_id=select_id,
                player_id=player_id,
                last_name=last_name,
                first_name=first_name,
                birthday=birthday,
                gender=gender,
                elo=int(elo),
            )
            player.create()
            logging.info("La base de test à été créé avec succès")