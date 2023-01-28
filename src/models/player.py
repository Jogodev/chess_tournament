import logging
import json
import secrets

DATA_FILE = "./database/players.json"


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

        with open(DATA_FILE, "a") as f:
            json.dump(
                self.serialize,
                f,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )

    def update(self):
        """Mise à jour du fichier json"""

        # TODO load db and all files
        # TODO Find the player in the Db loaded
        # TODO delete this player from db
        # TODO create the 'new' player
        # self.create()
        with open(DATA_FILE) as f:
            data = json.load(f)
            print(data)
        for player in data:
            print(player[1])
        # for player in players_dict:
        # print(player)

    def delete(self):
        """delete a specific player"""

        # TODO load db and all files
        # TODO Find the player in the Db loaded
        # TODO delete this player from db

    # with open(DATA_FILE) as f:
    #     players_dict = json.load(f)
    #     for player in players_dict:
    #         if player == players_dict["player_id"]:
    #             del player["GLASS"]

    @classmethod
    def find(self, key_value_dict: dict):
        """for a key_value_dict with {id : '12a'} find the palyer in the db and return an instace"""

        # TODO load db and all files
        # TODO Find the player in the Db loaded

        # TODO find in db where key_value_dict {id : '12a'} ==> find the good one
        # p_dict = {"firstname" : "alex", "lastname": "gaz"}
        # p = Player(**p_dict)

        # return p

    @classmethod
    def list_all(self) -> list:
        """return list of dict with all entries"""

        # TODO load DB
        # TODO transform in list of dict
        # TODO return the result

        # DEFAULT BEFORE CODING => RETURN EMPLY LIST
        return []

    @classmethod
    def delete_all(self) -> None:
        """delete all"""

        # TODO load DB
        # drop everything

    @classmethod
    def init_db(self):
        """boot db with vanessa"""

        p = Player(last_name="carlsen", elo=2890)
        p.create()
