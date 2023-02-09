
"""Main controller function"""
from src.views.main import main_menu_view
from src.views.player import *


def main_menu_controller():
    """"""
    choice = main_menu_view()

    if choice == "1":
        return "menu_player"
    elif choice == "2":
        print("vide pour le moment")
    elif choice == "b":
        print("retour au menu principal")
    else:
        raise AttributeError("aucun choix ne correspond")
