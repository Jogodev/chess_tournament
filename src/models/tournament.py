"""Tournament model"""

import logging
import secrets

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

    def update_current_round(self):
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
        if not tournament_list:
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
        self.status = "live"
        if len(self.player_list) != 8:
            raise AttributeError("8 joueurs necessaire")
        self.first_round()
        self.update_start_date()

    def first_round(self):
        """first round of the tournament"""

        if self.status == "live":
            self.id_current_round = 0

            game_list = self.compute_round()
            current_round = Round(
                tournament_id=self.tournament_id,
                round_name=secrets.token_hex(4),
                game_list=game_list,
            )
            self.round_list.append(current_round.round_id)
            current_round.create()
            self.update()
            self.update_current_round()

    @property
    def ranking(self):
        """Compute the ranking by score"""
        ranking = [(player, score) for player, score in self.scores.items()]
        ranking = sorted(ranking, key=lambda player: player[1], reverse=True)
        ranking = [player[0] for player in ranking]

        self.player_list = ranking

        return ranking

    @property
    def scores(self):
        """Get the scores of games in round"""

        scores = {player_id: 0 for player_id in self.player_list}
        if not self.status == "live" and not self.player_list:
            return {}

        elif self.status == "live" and not self.round_list:
            return scores

        # games = []
        # for round_id in self.round_list:
        #     round_find = Round.find(round_id)
        #     current_round = round_find[0]
        #     for game in current_round.game_list[0]:
        #         games.append(game[0])
        #         games.append(game[1])
        #
        # for game in games:
        #     scores[game[0]] += game[1]
        for round_id in self.round_list:
            round_find = Round.find(round_id)
            current_round = round_find[0]
            game_list = current_round.game_list
            for game in game_list[0]:
                scores[game[0][0]] += game[0][1]
                scores[game[1][0]] += game[1][1]
        return scores

    def have_already_played(self, player_id_1, player_id_2):
        """Return true if 2 players already play together"""

        all_round_game_list = []
        for round_id in self.round_list:
            round_find = Round.find(round_id)
            current_round = round_find[0]
            for game in current_round.game_list[0]:
                all_round_game_list.append([game[0][0], game[1][0]])

        candidate_game = (player_id_1, player_id_2)
        for game in all_round_game_list:
            if game == candidate_game:
                return True

        candidate_game = (player_id_2, player_id_1)
        for game in all_round_game_list:
            if game == candidate_game:
                return True

        return False

    def compute_round(self):
        """Define the rounds"""
        logging.warning("compute_round called")
        if not self.id_current_round:
            logging.warning("not self.id_current_round")
            # SHUFFLE


            game_list = []
            players_selected = []
            players_not_selected = [player for player in self.player_list]

            while len(players_not_selected) != 0:
                player_1 = players_not_selected[0]
                player_2 = players_not_selected[1]

                game = [(player_1, 0), (player_2, 0)]
                game_list.append(game)

                players_selected.extend([player_1, player_2])
                players_not_selected.remove(player_1)
                players_not_selected.remove(player_2)

            return game_list

        game_list = []
        players_selected = []
        self.player_list = self.ranking
        players_not_selected = [player for player in self.player_list]
        print(players_not_selected)

        index = 0
        while len(players_not_selected) != 0:
            player_1 = players_not_selected[index]

            if player_1 in players_selected:
                continue

            for player_id in self.player_list:
                if player_1 == player_id:
                    continue

                if player_id in players_selected:
                    continue

                already_played = self.have_already_played(player_1, player_id)
                if not already_played:
                    break

            game = [(player_1, 0), (player_id, 0)]
            game_list.append(game)

            players_selected.extend([player_1, player_id])
            players_not_selected.remove(player_1)
            players_not_selected.remove(player_id)

        return game_list

    def end_round(self):
        """End of a round"""
        round_id = self.round_list[self.id_current_round]
        round_find = Round.find(round_id)
        current_round = round_find[0]
        current_round.end_datetime = get_datetime()
        current_round.update()

        self.id_current_round += 1
        self.update_current_round()
        if len(self.round_list) == 4:
            logging.warning("Les 4 rondes ont été jouées, fin du tournoi")
            self.status = "closed"
            self.update()
            return self.scores

    def next_round(self):
        """All the rounds after the first"""

        game_list = self.compute_round()

        new_round = Round(
            tournament_id=self.tournament_id,
            round_name="round",
            game_list=game_list,
        )
        new_round.create()
        new_round.update()
        self.round_list.append(new_round.round_id)
        self.update()

    def end_tournament(self):
        """End of a tournament"""
        self.end_date = get_datetime()
        self.update_end_date()
