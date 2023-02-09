"""Main"""
from src.models.tournament import Tournament
from src.models.player import Player
from src.models.round import Round
from src.models.game import Game

from src.controllers.main import *
from src.controllers.player import *

controller_dict = {
    # Main menu
    "main_menu": main_menu_controller,
    # player
    "menu_player": menu_player_controller,
    "create_player": create_player_controller,
    "update_player": update_player_controller,
    "delete_player": delete_player_controller,
    # Tournament
    "tournament-menu": None,
}


def main():
    string_controller = main_menu_controller()


if __name__ == "__main__":
    main()
