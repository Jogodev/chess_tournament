"""Player model"""
import secrets
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

    @classmethod
    def update(cls, key, value, player_id):
        """Update player"""

        db = cls.table()
        db.all()
        query = Query()
        if key == "rank":
            db.update({key: int(value)}, query.player_id == player_id)
        else:
            db.update({key: value}, query.player_id == player_id)

    @classmethod
    def delete(cls, player_id):
        """delete a specific player"""

        db = cls.table()
        db.all()
        query = Query()
        return db.remove(query.player_id == player_id)

    @classmethod
    def find(cls, player_id):
        """Find a player by id"""
        db = cls.table()
        db.all()
        query = Query()
        player_find = db.search(query.player_id == player_id)
        return player_find

    @classmethod
    def list_all(cls):
        """return list of dict with all entries"""

        players_db = cls.table()
        # print(list(players_db.all()))
        players_db.all()

        ####### Ca OK mais mieux avec une comprehésenion de liste
        # p_list = [i for i in  players_db.all()]
        player_list = []

        for player in players_db:
            player_list.append(player)

        #### !!!!! :) :) Allo !!!! :) :) :)
        # return sans print
        # # et idem, meme si pas obligatoire je te conseille de faire
        # p_list = [Player(**i) for i in player_list]
        # return p_list
        # de return une liste de instance Player()
        return print(player_list)

    @classmethod
    def delete_all(cls):
        """delete all"""
        players_db = cls.table()
        return players_db.truncate()
