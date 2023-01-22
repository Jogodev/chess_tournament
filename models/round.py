import itertools
import random

class Ronde:

    def __init__(
        self,
        ronde_id,
        player_list: [],
        start_date,
        end_date
    ):
        self.ronde_id = ronde_id,
        self.player_list = player_list,
        self.start_date = start_date,
        self.end_date = end_date

    def pairring_player(self, player_list):
        """Création des paires de la 1ere ronde"""
        results_of_pairring = itertools.combinations(list(player_list), 2)
        return results_of_pairring


    def __repr__(self):
        return f"Match de la ronde n° {self.ronde_id}:"