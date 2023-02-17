from src.models.player import Player
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
            player_list: list = [{"last_name": "Alain", "rank": 1, "score": 0.0},
                                 {"last_name": "Stan", "rank": 2, "score": 0.0},
                                 {"last_name": "David", "rank": 3, "score": 0.0},
                                 {"last_name": "Scott", "rank": 4, "score": 0.0},
                                 {"last_name": "Kevin", "rank": 5, "score": 0.0},
                                 {"last_name": "Lucie", "rank": 6, "score": 0.0},
                                 {"last_name": "Elodie", "rank": 7, "score": 0.0},
                                 {"last_name": "Julie", "rank": 8, "score": 0.0}],
            description="",
    ):
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.id_current_round = -1
        self.round_list = 4
        self.player_list = player_list
        self.description = description
        self.tournaments_db = TinyDB("database/tournaments.json", indent=4, separators=(',', ': '))

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
        db.update({"current_round": self.id_current_round}, doc_ids=[self.tournament_id])

    def load_tournament(self):
        """"""

        db = self.tournaments_db
        db.all()
        tournament_list = []
        for tournament in db:
            tournament_list.append(tournament)
        print(tournament_list)
        return tournament_list

    def __repr__(self):
        return (
            f"Le tournoi n° {self.id} {self.name} viens de commencé à {self.location}"
        )

    def sort_players_by_rank(self):
        """"""
        sortedPlayersByRank = sorted(self.player_list, key=lambda players: players["rank"])
        return sortedPlayersByRank

    def sort_players_by_score(self):
        """"""
        sortedPlayersByScore = sorted(self.player_list, key=lambda players: players["score"])
        return sortedPlayersByScore

    def pairring(self):
        player

    def add_round(self):
        ronde = Round(player_list)
        self.round_list.append(ronde)
        self.id_current_round = id
