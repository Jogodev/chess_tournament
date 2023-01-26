import json
import secrets

DATA_FILE = "./database/players.json"


class Player:
    """Player Class """

    def __init__(
        self,
        lastname: str,
        firstname: str = "-",
        birthday: str = "-",
        sex: str = "-",
        elo: int = 0,
        player_id: str = "-",
    ):
        """init method """

        self.lastname = lastname.upper()
        self.firstname = firstname.capitalize()
        self.birthday = birthday
        self.elo = elo

        if player_id == "-":
            player_id = secrets.token_hex(4)
        self.player_id = player_id

    def __repr__(self):
        """repr method """

        return f"Player({self.__dict__})"

    def serialize_player(self):
        """Formatage d'un joueur"""

        return self.__dict__

    def create(self):
        """Sauvegarde d'un joueur"""

        with open(DATA_FILE, "a") as f:
            json.dump(
                self.serialize_player(),
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

    def delete(self):
        """delete a specific player """

        # TODO load db and all files
        # TODO Find the player in the Db loaded
        # TODO delete this player from db

    @classmethod
    def find(self, key_value_dict: dict):
        """ for a key_value_dict with {id : '12a'} find the palyer in the db and return an instace"""

        # TODO load db and all files
        # TODO Find the player in the Db loaded

        # TODO find in db where key_value_dict {id : '12a'} ==> find the good one
        # p_dict = {"firstname" : "alex", "lastname": "gaz"}
        # p = Player(**p_dict)

        # return p

    @classmethod
    def list_all(self):
        """return list of dict with all entries """

        # TODO load DB
        # TODO transform in list of dict
        # TODO return the result

    @classmethod
    def delete_all(self):
        """delete all """

        # TODO load DB
        # drop everything
