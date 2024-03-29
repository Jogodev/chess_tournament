"""Reports controllers"""

from src.models.player import Player
from src.models.tournament import Tournament
from src.views.report import (
    menu_report_view,
    all_players_view, all_tournaments_view, players_in_tournament_view,
    rounds_and_games_tournament_view, one_tournament_choice_view, report_choice_view
)


def menu_report_controller(data_dict):
    """Menu of the reports"""
    choice = menu_report_view()

    if choice == "1":
        return "all_players_report", data_dict
    elif choice == "2":
        return "all_tournaments_report", data_dict
    elif choice == "3":
        return "one_tournament_choice", data_dict
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


def one_tournament_choice_controller(data_dict):
    """Name and dates of a tournament"""
    tournaments = Tournament.load_tournaments()
    tournament_id = one_tournament_choice_view(tournaments)
    tournament = Tournament.find(tournament_id)
    data_dict = tournament
    if tournament:
        return "report_choice", data_dict
    elif tournament_id == "b":
        return "menu_report", data_dict
    else:
        print("\nSaisie non valide")
        return "all_tournaments_report", data_dict


def report_choice_controller(data_dict):
    """Choice between some reports"""
    tournament = data_dict[0]
    choice = report_choice_view(tournament.serialize())
    if choice == "1":
        return "players_in_tournament", data_dict
    elif choice == "2":
        return "rounds_and_games", data_dict
    elif choice == "b":
        return "one_tournament_choice", data_dict
    else:
        print("\nSaisie non valide")
        return "report_choice", data_dict


def players_in_tournament_controller(data_dict):
    """Players in a tournament sort by last name"""
    tournament = data_dict[0]
    players = tournament.all_players_attributes()
    choice = players_in_tournament_view(players)
    if choice == "b":
        return "report_choice", data_dict
    else:
        print("\nSaisie non valide")
        return "players_in_tournament", data_dict


def rounds_and_games_tournament_controller(data_dict):
    """rounds and games of a tournament"""
    tournament = data_dict[0]
    rounds = tournament.all_rounds()[0]
    players = tournament.all_rounds()[1]
    results = tournament.all_rounds()[2]
    game_list = tournament.all_rounds()[3]
    choice = rounds_and_games_tournament_view(rounds, players, results, game_list)
    if choice == "b":
        return "report_choice", data_dict
    else:
        print("\nSaisie non valide")
        return "rounds_and_games", data_dict
