"""Tournament model"""

import logging

from tinydb import TinyDB, Query

from helpers.time import get_datetime
from src.models.round import Round
from src.models.player import Player


class Tournament:
    """Tournament class"""

    db_file = "./database/tournaments.json"

    def __init__(
            self,
            name: str,
            tournament_id: str = "",
            location: str = "",
            start_date: str = "",
            end_date: str = "",
            id_current_round: int = -1,
            round_list: list = [],
            total_rounds: int = 4,
            player_list: list = [],
            description: str = "-",
            status: str = "created",
    ) -> None:
        self.tournament_id = tournament_id
        self.name = name.upper()
        self.location = location.capitalize()
        self.start_date = start_date
        self.end_date = end_date
        self.id_current_round = id_current_round
        self.round_list = round_list
        self.total_rounds = total_rounds
        self.player_list = player_list
        self.description = description
        self.status = status

    @classmethod
    def table(cls):
        """Tournament db"""
        return TinyDB(cls.db_file, indent=4, separators=(",", ": "))

    def serialize(self):
        """Serialize the tournament"""
        return self.__dict__

    def create(self):
        """Save tournament"""

        db = self.table()
        self.tournament_id = db.insert(self.serialize())
        db.update(
            {"tournament_id": str(self.tournament_id)}, doc_ids=[self.tournament_id]
        )
        logging.info(f"Tournoi {self.name} créé à {self.location}")

    def update(self):
        """Update tournament"""
        db = self.table()
        query = Query()
        db.update(
            {"player_list": self.player_list}, query.tournament_id == self.tournament_id
        )
        db.update(
            {"total_rounds": self.total_rounds},
            query.tournament_id == self.tournament_id,
        )
        db.update({"round_list": self.round_list}, query.tournament_id == self.tournament_id)
        db.update({"status": self.status}, query.tournament_id == self.tournament_id)

    @classmethod
    def load_tournaments(cls):
        """Load tournament"""

        db = cls.table()
        tournament_list = [tournament for tournament in db.all()]
        if tournament_list == []:
            print("Aucun tournoi dans la base de données")
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

    def add_player(self, player_dict: dict):
        """Add a player in tournament"""

        player_id = player_dict["player_id"]
        if (player_id not in self.player_list) and (self.status == "created"):
            self.warning = logging.warning(f"Nous allons ajouter {player_dict} ")
            self.player_list.append(player_id)
            self.update()
            logging.warning("Joueur ajouté au tournoi")
        elif player_id in self.player_list:
            logging.warning("Ce joueur est déjà dans ce tournoi")
        else:
            logging.warning(
                f"Ce tournoi est en status {self.status} et n'accepte plus de joueur"
            )

        if len(self.player_list) == 2:
            logging.warning(
                "ON A 2 JOUEURS == > CLOTURE DES INSCRIPTION VERSION de TESt"
            )
            self.status = "ready"
            self.update()

        return None

    def add_players(self, player_list):
        """"""
        for player in player_list:
            self.add_player(player)

    def start_tournament(self):
        """Beginning of the tournament"""
        self.start_date = get_datetime()
        self.end_date = "Tournoi en cours"
        self.status = "in progress"
        if len(self.player_list) != 2:
            raise AttributeError("Travail sur 2 joueurs uniquement")
        self.id_current_round = 0
        self.first_round()
        self.update_start_date()

    def first_round(self):
        """first round"""
        self.id_current_round += 1
        game_1 = ([self.player_list[0], -1], [self.player_list[1], -1])
        current_round = Round(self.tournament_id, "round_1", [game_1], get_datetime(), "en cours")
        self.round_list.append(round.round_id)
        self.update_round()
        current_round.create()
        self.update()

    def update_round(self):
        """Update a round of the tournament"""

        db = self.table()
        query = Query()
        db.update(
            {"id_current_round": self.id_current_round},
            query.tournament_id == self.tournament_id,
        )

    def update_start_date(self):
        """Set the datetime when the first round begin"""
        db = self.table()
        query = Query()
        db.update(
            {"start_date": self.start_date}, query.tournament_id == self.tournament_id
        )

    def update_end_date(self):
        """Set the datetime when the tournament finish"""
        db = self.table()
        query = Query()
        db.update(
            {"end_date": self.end_date}, query.tournament_id == self.tournament_id
        )

    def get_score(self):
        """"""

        pass

    def update_score(self):
        """"""
        pass

    def end_round(self):
        """"""
        pass

    def resume_tournament(self):
        """"""
        pass
