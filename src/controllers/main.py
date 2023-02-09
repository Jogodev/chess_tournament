"""Main controller functions"""
from src.views.main import main_menu_view



def main_menu_controller():
    """"""
    choice = main_menu_view()

    if choice == "1":
        return "menu_player"
    elif choice == "2":
        return "tournament_menu"
    elif choice == "b":
        return "main_menu"

