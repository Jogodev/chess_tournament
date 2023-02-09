"""Player controller"""
from src.views.player import *


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
    else:
        raise AttributeError("Aucun choix ne correspond")

def create_player_controller():

    player_dict = create_player_view()


def update_player_controller():

    player = update_player_view()


def delete_player_controller():

    player = delete_player_view()