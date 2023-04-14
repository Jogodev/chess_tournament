"""Reports controllers"""

from src.models.player import Player
from src.models.tournament import Tournament
from src.views.report import (
    menu_report_view,
    all_players_view, all_tournaments_view, one_tournament_report_view, players_in_tournament_view, \
    rounds_and_games_tournament_view
)


def menu_report_controller(data_dict):
    """Menu of the reports"""
    choice = menu_report_view()

    if choice == "1":
        return "all_players_report", data_dict
    elif choice == "2":
        return "all_tournaments_report", data_dict
    elif choice == "3":
        return "", data_dict
    elif choice == "4":
        return "", data_dict
    elif choice == "5":
        return "", data_dict
    elif choice == "b":
        return "main_menu", data_dict


def all_players_report_controller(data_dict):
    """all players sort by lastname"""
    players = Player.list_all()
    sort_players = sorted(players, key=lambda player: player['last_name'])
    choice = all_players_view(sort_players)
    if choice == "b":
        return "menu_report", data_dict
    else:
        print("\nSaisie non valide")
        return "all_players_report", data_dict


def all_tournaments_report_controller(data_dict):
    """all tournaments in database"""
    tournaments = Tournament.load_tournaments()
    choice = all_tournaments_view(tournaments)
    if choice == "b":
        return "menu_report", data_dict
    else:
        print("\nSaisie non valide")
        return "all_tournaments_report", data_dict


def one_tournament_report_controller(data_dict):
    """Name and dates of a tournament"""
    choice = one_tournament_report_view()


def players_in_tournament_controller(data_dict):
    """Players in a tournament sort by last name"""
    choice = players_in_tournament_view(tournament)


def rounds_and_games_tournament_controller(data_dict):
    """rounds and games of a tournament"""
    choice = rounds_and_games_tournament_view()
