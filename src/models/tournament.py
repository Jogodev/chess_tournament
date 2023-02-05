
from tinydb import TinyDB
import secrets


class Tournament:
    def __init__(
        self,
        name: str,
        tournament_id: str = secrets.token_hex(8),
        location: str = '',
        start_date: str = '',
        end_date: str = '',
        time_control: int = '',
        player_list: list = [],
        description="",
    ):
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.id_current_round = -1
        self.round_list = []
        self.time_control = time_control
        self.player_list = player_list
        self.description = description
        self.tournaments_db = TinyDB("database/tournaments.json", sort_keys=True, indent=4, separators=(',', ': '))

    def serialize_tournament(self):
        """"""

        return {
            "id": self.tournament_id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_round": self.id_current_round,
            "round_list": self.round_list,
            "player_list": self.player_list,
            "time_control": self.time_control,
            "description": self.description,
        }

    def save_tournament(self):
        """ Save tournament """

        db = self.tournaments_db
        db.insert(self.serialize_tournament())

    def update_tournament(self):
        """"""

        db = self.tournaments_db
        db.all()
        db.update({"time_control": self.time_control}, doc_ids=[self.tournament_id])
        db.update({"current_round": self.id_current_round}, doc_ids=[self.tournament_id])



    def load_tournament(self):
        """"""


    def __repr__(self):
        return (
            f"Le tournoi n° {self.id} {self.name} viens de commencé à {self.location}"
        )

    def add_round(self):
        ronde = Ronde(player_list)
        self.ronde_list.append(ronde)
        self.id_current_round = id
