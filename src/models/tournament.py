"""Tournament model"""
import datetime
from random import randint

from src.models.round import Round
from tinydb import TinyDB, Query

import secrets, logging


class Tournament:
    """Tournament class"""

    def __init__(
            self,
            name: str,
            tournament_id: str = "",
            location: str = "",
            start_date: str = str(datetime.datetime.now()),
            end_date: str = "tournoi en cours",
            id_current_round: int = -1,
            round_list: int = 4,
            player_list: list = [],
            description: str = "-",
            status: str = "created",
    ):
        self.tournament_id = tournament_id
        self.name = name.upper()
        self.location = location.capitalize()
        self.start_date = start_date
        self.end_date = end_date
        self.id_current_round = id_current_round
        self.round_list = round_list
        self.player_list = player_list
        self.description = description
        self.status = status

    @classmethod
    def table(cls):
        """Tournament db"""
        return TinyDB("database/tournaments.json", indent=4, separators=(",", ": "))

    def serialize(self):
        """Serialize the tournament"""
        return self.__dict__

    def save_tournament(self):
        """Save tournament"""

        db = self.table()
        self.tournament_id = db.insert(self.serialize())
        db.update(
            {"tournament_id": str(self.tournament_id)}, doc_ids=[self.tournament_id]
        )
        logging.info(f"Tournoi {self.name} créé à {self.location}")

    def update_tournament(self):
        """Update tournament"""
        db = self.table()
        db.update({"player_list": self.player_list}, Query().tournament_id == self.tournament_id)
        db.update({"id_current_round": self.id_current_round}, Query().tournament_id == self.tournament_id)
        db.update({"round_list": self.round_list}, Query().tournament_id == self.tournament_id)

    @classmethod
    def load_tournaments(cls):
        """Load tournament"""

        db = cls.table()
        tournament_list = [tournament for tournament in db.all()]
        logging.info(tournament_list)
        return tournament_list

    @classmethod
    def find(cls, tournament_id):
        """find a tournament"""
        db = cls.table()
        db.all()
        query = Query()
        tournament_find = db.search(query.tournament_id == tournament_id)
        tournament_list = [
            Tournament(**dict(tournament)) for tournament in tournament_find
        ]
        return tournament_list

    def __repr__(self):
        return f"Tournoi {self.__dict__}"

    def sort_players_by_rank(self):
        """Sort players by rank"""
        sorter_players_by_rank = sorted(
            self.player_list, key=lambda players: players["elo"]
        )
        return sorter_players_by_rank

    def sort_players_by_score(self):
        """Sort players by score"""
        sorted_players_by_score = sorted(
            self.player_list, key=lambda players: players["score"]
        )
        return sorted_players_by_score

    def add_player(self, player_id):
        """"""
        if (player_id not in self.player_list) and (self.status == "created"):
            self.player_list.append(player_id)
            self.update_tournament()
            logging.info("Joueur ajouté au tournoi")

    def add_players(self, player_list):
        """"""
        for player in player_list:
            self.add_player(player)

    def start_tournament(self):
        """"""

        self.status = "live"
        if len(self.player_list) != 2:
            raise AttributeError("Travail sur 2 joueurs uniquement")
        match_1 = ([self.player_id[0], -1], [self.player_id[1], -1])
        round_1 = [match_1]
        self.round_list = [round_1]
        self.round_id = 0

    def resume_tournament(self):
        """"""
        pass

    def end_round(self):
        """"""
        pass

    def add_round(self):
        """"""
        ronde = Round(self.player_list)
        self.round_list.append(ronde)
        self.id_current_round = id
