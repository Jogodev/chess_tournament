"""Tournament model"""

import logging

from tinydb import TinyDB, Query

from helpers.time import get_datetime
from src.models.round import Round


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

    def update_round(self):
        """Update a round of the tournament"""

        db = self.table()
        query = Query()
        db.update(
            {"id_current_round": self.id_current_round},
            query.tournament_id == self.tournament_id,
        )

    @classmethod
    def load_tournaments(cls):
        """Load tournament"""

        db = cls.table()
        tournament_list = [tournament for tournament in db.all()]
        if tournament_list == []:
            print("Aucun tournoi dans la base de données, [b] pour revenir au menu principal")
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

    def sort_players_by_score(self):
        """Sort players by score"""
        sorted_players_by_score = sorted(
            self.player_list, key=lambda x: x('score')
        )
        return sorted_players_by_score

    def add_player(self, player_dict: dict):
        """Add a player in tournament"""

        player_id = player_dict["player_id"]
        if (player_id not in self.player_list) and (self.status == "created"):
            self.player_list.append(player_id)
            self.update()
            logging.warning("Joueur ajouté au tournoi")
        elif player_id in self.player_list:
            logging.warning("Ce joueur est déjà dans ce tournoi")
        else:
            logging.warning(
                f"Ce tournoi est en status {self.status} et n'accepte plus de joueur"
            )

        if len(self.player_list) == 8:
            logging.warning(
                "ON A 8 JOUEURS == > CLOTURE DES INSCRIPTION VERSION de TEST"
            )
            self.status = "ready"
            self.update()

        return None

    def add_players(self, player_list):
        """Add player in the tournament"""
        for player in player_list:
            self.add_player(player)

    def start_tournament(self):
        """Beginning of the tournament"""
        self.start_date = get_datetime()
        self.end_date = "Tournoi en cours"
        self.status = "in progress"
        if len(self.player_list) != 8:
            raise AttributeError("8 joueurs necessaire")
        self.id_current_round = 0
        self.first_round()
        self.update_start_date()

    def first_round(self):
        """first round of the tournament"""
        self.id_current_round += 1
        self.update_round()
        game_1 = ([self.player_list[0], -1], [self.player_list[1], -1])
        game_2 = ([self.player_list[2], -1], [self.player_list[3], -1])
        game_3 = ([self.player_list[4], -1], [self.player_list[5], -1])
        game_4 = ([self.player_list[6], -1], [self.player_list[7], -1])
        game_of_first_round = [game_1, game_2, game_3, game_4]
        current_round = Round(self.tournament_id, "round_1", game_of_first_round, get_datetime(),
                              "en cours")
        self.round_list.append(current_round.round_id)
        current_round.create()
        self.update()

    def next_round(self):
        """All rounds after the first"""
        #
        # Appeler methode score
        # Triez les joueurs par score
        # pour le joueur 0 va affronter le joueur 1 de la liste s'il n'ont pas deja jouer ensemble
        # game_already_play(p_id1, p_id2) qui renvoi true ou false
            # self.id_current_round += 1
        # self.update_round()

        scores = self.scores
        sort_players = sorted(scores.items(), key=lambda player_score: player_score[1], reverse=True)
        print(sort_players)
        new_games = []

        if self.game_already_played(sort_players[0][0], sort_players[1][0]):
            new_games.append([sort_players[0], sort_players[1]])
        elif not self.game_already_played(sort_players[0][0], sort_players[1][0]):
            self.game_already_played(sort_players[0][0], sort_players[2][0])

        print(new_games)

    @property
    def scores(self):
        """Get the scores of games in round"""
        # Si le tournoi n'a pas démarrer revoyer un dict vide
        # Le tournoi à démarré mais les rondes n'ont pas été calculé self.ronde_list = vide
        scores = {player_id: 0 for player_id in self.player_list}
        if not self.status == "in progress" and not self.player_list:
            return {}
        elif self.status == "in progress" and not self.round_list:
            return scores
        games = []
        for round_id in self.round_list:
            round_find = Round.find(round_id)
            current_round = round_find[0]
            print(current_round)
            for game in current_round.game_list[0]:
                games.append(game[0])
                games.append(game[1])

        for game in games:
            scores[game[0]] += game[1]
        return scores

    def game_already_played(self, player_id_1, player_id_2):
        """Return true if 2 players already play together"""
        all_round_games = []
        for round_id in self.round_list:
            round_find = Round.find(round_id)
            current_round = round_find[0]
            print(current_round)
            for game in current_round.game_list[0]:
                all_round_games.append([game[0][0], game[1][0]])
        if ([player_id_1, player_id_2] or [player_id_2, player_id_1]) not in all_round_games:
            return True
        else:
            return False

    def end_round(self):
        """"""
        pass

    def resume_tournament(self):
        """"""
        pass
