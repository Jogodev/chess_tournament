from models.tournament import Tournament
from models.player import Player
from models.round import Ronde
from models.game import Game
import itertools
import json


def main():

    player_1 = Player(1, "lafont", "julie", "25/02/1988")
    player_2 = Player(2, "gage", "john", "25/02/1978")
    player_3 = Player(3, "Alain", "Fournier", "25/02/1958")
    player_4 = Player(4, "dupont", "vanessa", "25/02/1991")
    player_5 = Player(4, "georges", "Yves", "25/02/1991")
    player_6 = Player(4, "sebastien", "bernard", "25/02/1991")
    player_7 = Player(4, "renaud", "jean", "25/02/1991")
    player_8 = Player(4, "dupont", "vanessa", "25/02/1991")
    player_1.save_player()
    player_2.save_player()
    player_3.save_player()
    player_4.save_player()
    player_list = {player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8}
    first_ronde = Ronde(1, player_list, '10/02/2023', '10/02/2023')
    print(first_ronde)
    first_tournament = Tournament("Pemier tournoi", "Paris", "21/02/2023", "21/02/2023", player_list, "C'est parti")
    print(first_tournament)


if __name__ == "__main__":
    main()
