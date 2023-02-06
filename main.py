
from src.models.tournament import Tournament
from src.models.player import Player
from src.models.round import Round
from src.models.game import Game
import itertools


def main():
    # player1 = Player(1, "Matt")
    # player2 = Player(2, "Patrick")
    # player3 = Player(3, "David")
    # player1.create()
    # player2.create()
    # player3.create()
    # player3.update_player("Fred")
    # new_tournament = Tournament("Nouveau tournoi")
    # new_tournament.save_tournament()
    # new_tournament.load_tournament()
    first_round = Round(1, "1ere ronde")
    print(first_round)


if __name__ == "__main__":
    main()
