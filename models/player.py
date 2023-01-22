import json


class Player:
    def __init__(
            self,
            player_id: str,
            lastname: str,
            firstname: str,
            birthday: str,
    ):
        self.player_id = player_id
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.score = 0.0

    def __repr__(self):
        return f"Le joueur suivant a été créé {self.lastname} {self.firstname}"

    def serialize_player(self):
        """Formatage d'un joueur"""
        player = {
            "id": self.player_id,
            "Nom": self.lastname,
            "Prénom": self.firstname,
            "Date de naissance": self.birthday,
            "Score": self.score,
        }
        return player

    def save_player(self):
        """Sauvegarde d'un joueur"""
        with open("database/players.json", 'a') as players_database:
            json.dump(self.serialize_player(), players_database, ensure_ascii=False, indent=2, sort_keys=True)


    def update_player(self):
        """Mise à jour du fichier json"""
        pass



