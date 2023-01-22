import json
import secrets


class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        player_list,
        description="",
    ):
        self.id = secrets.token_hex(8)
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.id_current_round = -1
        self.round_list = []
        self.player_list = player_list
        self.description = description

    def serialize_tournament(self):
        tournament = {
            "id": self.id,
            "Nom": self.name,
            "Lieu": self.location,
            "Date de début": self.start_date,
            "Date de fin": self.end_date,
            "Ronde en cours": self.id_current_round,
            "Liste des rondes": self.round_list,
            "Liste des joueurs": self.player_list,
            "Notes": self.description,
        }
        return tournament

    def save_tournament(self):
        with open("databases/tournament", "a") as database_tournament:
            json.dump(self.serialize_tournament(), database_tournament, ensure_ascii=False)

    def add_round(self):
        ronde = Ronde(player_list)
        self.ronde_list.append(ronde)
        self.id_current_round = id
