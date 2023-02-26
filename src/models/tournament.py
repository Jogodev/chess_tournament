"""Tournament model"""
import datetime
from random import randint

from src.models.player import Player
from src.models.round import Round
from tinydb import TinyDB, Query

import secrets, logging


class Tournament:
    """Tournament class"""

    def __init__(
            self,
            name: str,
            tournament_id: str = '',
            select_id: int = randint(0, 30),
            location: str = '',
            start_date: str = str(datetime.datetime.now()),
            end_date: str = "tournoi en cours",
            id_current_round: int = -1,
            round_list: int = 4,
            player_list: list = [],
            description: str = "-",
    ):
        self.tournament_id = tournament_id if tournament_id else secrets.token_hex(5)
        self.select_id = select_id
        self.name = name.upper()
        self.location = location.capitalize()
        self.start_date = start_date
        self.end_date = end_date
        self.id_current_round = id_current_round
        self.round_list = round_list
        self.player_list = player_list
        self.description = description

    @classmethod
    def table(cls):
        """Tournament db"""
        return TinyDB("database/tournaments.json", indent=4, separators=(',', ': '))

    def serialize(self):
        """Serialize the tournament"""
        return self.__dict__

    def save_tournament(self):
        """ Save tournament """

        db = self.table()
        db.insert(self.serialize())
        logging.info(f"Tournoi {self.name} créé à {self.location}")

    @classmethod
    def load_tournaments(cls):
        """Load tournament"""

        db = cls.table()
        db.all()
        tournament_list = []
        for tournament in db:
            tournament_list.append(tournament)
        print(tournament_list)
        return tournament_list

    @classmethod
    def find(cls, tournament_id):
        """find a tournament"""
        db = cls.table()
        db.all()
        query = Query()
        tournament_find = db.search(query.tournament_id == tournament_id)
        tournament_list = [Tournament(**dict(tournament)) for tournament in tournament_find]
        return tournament_list

    def __repr__(self):
        return f"Tournoi {self.__dict__}"

    def sort_players_by_rank(self):
        """Sort players by rank"""
        sorter_players_by_rank = sorted(self.player_list, key=lambda players: players["rank"])
        return sorter_players_by_rank

    def sort_players_by_score(self):
        """Sort players by score"""
        sorted_players_by_score = sorted(self.player_list, key=lambda players: players["score"])
        return sorted_players_by_score

    def add_round(self):
        """"""
        ronde = Round(player_list)
        self.round_list.append(ronde)
        self.id_current_round = id
