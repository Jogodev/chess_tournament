"""Main controller functions"""
from src.views.main import main_menu_view


def main_menu_controller(data_dict):
    """Main menu"""
    choice = main_menu_view()

    if choice == "1":
        return "menu_player", data_dict
    elif choice == "2":
        return "menu_tournament", data_dict
    elif choice == "3":
        return "menu_report", data_dict
    else:
        print("\nSaisie non valide\n")
        return "main_menu", data_dict
