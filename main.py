"""Main"""

from src.controllers.main import main_menu_controller
from src.controllers.player import menu_player_controller, create_player_controller, update_player_controller, \
    delete_player_controller
from src.controllers.tournament import menu_tournament_controller, create_tournament_controller

controller_dict = {
    # Main menu
    "main_menu": main_menu_controller,
    # player
    "menu_player": menu_player_controller,
    "create_player": create_player_controller,
    "update_player": update_player_controller,
    "delete_player": delete_player_controller,
    # Tournament
    "tournament_menu": menu_tournament_controller,
    "create_tournament": create_tournament_controller,
    "update_tournament": update_player_controller,
}


def main():
    """"""
    string_controller = main_menu_controller()

    while True:
        controller = controller_dict[string_controller]
        string_controller = controller()


if __name__ == "__main__":
    main()
