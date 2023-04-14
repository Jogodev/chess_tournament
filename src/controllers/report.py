"""Reports controllers"""

from src.models.player import Player
from src.models.tournament import Tournament
from src.views.report import (
    menu_report_view,
    all_players_view,
)


def menu_report_controller(data_dict):
    """Menu of the reports"""
    choice = menu_report_view()

    if choice == "1":
        return "all_players_report", data_dict
    elif choice == "2":
        return "", data_dict
    elif choice == "3":
        return "", data_dict
    elif choice == "4":
        return "", data_dict
    elif choice == "5":
        return "", data_dict
    elif choice == "b":
        return "main_menu", data_dict
    else:
        print("\nSaisie non valide\n")
        return "menu_report", data_dict


def all_players_report_controller(data_dict):
    """all players sort by lastname"""
    players = Player.list_all()
    sort_players = sorted(players, key=lambda player: player['last_name'])
    choice = all_players_view(sort_players)
    if choice == "b":
        return "menu_reports", data_dict
    else:
        print("\nSaisie non valide")
        return "all_players", data_dict

def all_tournaments(data_dict):
    """all tournaments in database"""
    tournament = Tournament.load_tournaments()