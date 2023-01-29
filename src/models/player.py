import logging
import json
import secrets

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

    def __repr__(self):
        """repr method"""

        return f"Player({self.__dict__})"

    @property
    def serialize(self):
        """Formatage d'un joueur"""

        return self.__dict__



    def create(self):
        """Sauvegarde d'un joueur"""

        with open(PLAYERS_DATA_FILE, "a") as f:
            json.dump(
                self.serialize,
                f,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
                )

    def update(self):
        """Mise à jour du fichier json"""
        last_name = input('entrez le nom du joueur :')
        # TODO load db and all files
        with open(PLAYERS_DATA_FILE) as f:
            players_db = json.load(f)
            print(players_db)
        # TODO Find the player in the Db loaded
        for player in players_db:
            if player['lastname'] == last_name:
                return player
        # TODO delete this player from db
        if last_name == players_db["last_name"]:
            del players_db['last_name']
        # TODO create the 'new' player
        self.create()



    def delete(self):
        """delete a specific player"""
        last_name = input('entrez le nom du joueur que vous voulez supprimez')
        # TODO load db and all files
        with open(PLAYERS_DATA_FILE) as f:
            players_db = json.load(f)
        # TODO Find the player in the Db loaded
            for player in players_db:
                if player['lastname'] == last_name:
                    return player
        # TODO delete this player from db
        if last_name == players_db["last_name"]:
            del players_db["last_name"]





    @classmethod
    def find(self, key_value_dict: dict):
        """for a key_value_dict with {id : '12a'} find the palyer in the db and return an instace"""
        _id = input("Entrez l'id du joueur :")
        # TODO load db and all files
        with open(PLAYERS_DATA_FILE) as f:
            player_db = json.load(f)
        # TODO Find the player in the Db loaded
            for player in player_db:
                if player_db["player_id"] == _id:
                    return player
        # TODO find in db where key_value_dict {id : '12a'} ==> find the good one
            for player in player_db:
                if player_db["player_id"] == _id:
                    return player

        # p_dict = {"firstname" : "alex", "lastname": "gaz"}
        # p = Player(**p_dict)

        # return p

    @classmethod
    def list_all(self) -> list:
        """return list of dict with all entries"""

        # TODO load DB
        with open(PLAYERS_DATA_FILE) as f:
            player_db = json.load(f)
        # TODO transform in list of dict

        # TODO return the result

        # DEFAULT BEFORE CODING => RETURN EMPTY LIST
        return []

    @classmethod
    def delete_all(self) -> None:
        """delete all"""

        # TODO load DB
        with open(PLAYERS_DATA_FILE) as f:
            player_db = json.load(f)
        # drop everything
            del player_db
    @classmethod
    def init_db(self):
        """boot db with vanessa"""

        p = Player(last_name="carlsen", elo=2890)
        p.create()
