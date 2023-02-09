"""Player controller"""
from src.views.player import menu_player_view, create_player_view, update_player_view, delete_player_view
from src.models.player import Player


def menu_player_controller():
    """"""
    choice = menu_player_view()

    if choice == "1":
        return "create_player"
    elif choice == "2":
        return "update_player"
    elif choice == "3":
        return "delete_player"
    elif choice == "b":
        return "main_menu"

    raise AttributeError("Aucun choix ne correspond")


def create_player_controller():
    """"""
    player = create_player_view()

    print(player)
    return "menu_player1"


def update_player_controller():

    player = update_player_view()


def delete_player_controller():

    player = delete_player_view()