from models.tournament import Tournament
from models.player import Player
from models.round import Ronde
from models.game import Game
import itertools
import json


def main():

    player_1 = Player("lafont", "julie", "25/02/1988")
    player_2 = Player("gage", "john", "25/02/1978")
    player_3 = Player("Alain", "Fournier", "25/02/1958")
    player_4 = Player("dupont", "vanessa", "25/02/1991")
    player_5 = Player("georges", "Yves", "25/02/1991")
    player_6 = Player("sebastien", "bernard", "25/02/1991")
    player_7 = Player("renaud", "jean", "25/02/1991")
    player_8 = Player("dupont", "vanessa", "25/02/1991")
    player_1.save_player()
    player_2.save_player()
    player_3.save_player()
    player_4.save_player()
    player_5.save_player()
    player_6.save_player()
    player_7.save_player()
    player_8.save_player()
    player_list = [
        player_1.firstname + " " + player_1.lastname,
        player_2.firstname + " " + player_2.lastname,
        player_3.firstname + " " + player_3.lastname,
        player_4.firstname + " " + player_4.lastname,
        player_5.firstname + " " + player_5.lastname,
        player_6.firstname + " " + player_6.lastname,
        player_7.firstname + " " + player_7.lastname,
        player_8.firstname + " " + player_8.lastname,
        ]

    first_ronde = Ronde(1, player_list, "10/02/2023", "10/02/2023")
    print(first_ronde)
    first_tournament = Tournament(
        "Pemier tournoi",
        "Paris",
        "21/02/2023",
        "21/02/2023",
        player_list,
        "C'est parti",
    )
    print(first_tournament)
    first_tournament.save_tournament()
    first_tournament.load_tournament()


if __name__ == "__main__":
    main()
