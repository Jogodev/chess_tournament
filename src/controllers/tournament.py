"""Tournament controller"""
import logging

from src.views.tournament import\
    (menu_tournament_view,
     create_tournament_view,
     add_players_now_view,
     load_tournaments_view,
     add_players_view,
     load_one_tournament_view,
     load_one_tournament_ready_view,
     start_tournament_view,
     first_round_view,
     )

from src.models.tournament import Tournament
from src.models.player import Player


def menu_tournament_controller(data_dict):
    """Menu tournament controller"""
    choice = menu_tournament_view()

    if choice == "1":
        return "create_tournament", data_dict
    elif choice == "2":
        return "load_tournaments", data_dict
    elif choice == "2":
        return "add_players_now", data_dict
    elif choice == "b":
        return "main_menu", data_dict
    else:
        print("\nSaisie non valide\n")
        return "menu_tournament", data_dict


def create_tournament_controller(data_dict):
    """Create a controller"""
    tournament_dict = create_tournament_view()
    tournament = Tournament(**tournament_dict)
    tournament.create()
    data_dict = tournament

    return "add_players_now", data_dict


def load_tournaments_controller(data_dict):
    """Load all tournaments"""
    tournament_list = Tournament.load_tournaments()
    tournament_id = load_tournaments_view(tournament_list)
    tournament = Tournament.find(tournament_id)
    print(tournament)
    data_dict = tournament_id

    if (tournament != []) and (tournament[0].serialize() in tournament_list):
        return "load_one_tournament", data_dict
    else:
        print("\nAucun tournoi ne correspond à cet id\n")
        return "load_tournaments", data_dict


def load_one_tournament_controller(data_dict):
    """Load one tournament"""
    tournament_id = data_dict
    tournament_list = Tournament.find(tournament_id)
    tournament = tournament_list[0]
    data_dict = tournament
    status = data_dict.status
    if status == "ready":
        return "load_one_tournament_ready", data_dict

    choice = load_one_tournament_view(tournament.serialize())

    if choice == "y":
        return "add_players", data_dict
    elif choice == "n":
        return "menu_tournament", data_dict
    else:
        print("\nSaisie non valide")
        return "load_one_tournament", data_dict


def load_one_tournament_ready_controller(data_dict):
    """Load a tournament who ready"""
    choice = load_one_tournament_ready_view(data_dict.serialize())
    print(choice)
    if choice == "y":
        return "start_tournament", data_dict
    elif choice == "n":
        return "menu_tournament", data_dict
    else:
        print("\nSaisie non valide")
        return "load_one_tournament_ready", data_dict


def add_players_now_controller(data_dict):
    """add players"""
    choice = add_players_now_view()

    if choice == "y":
        return "add_players", data_dict
    elif choice == "n":
        return "menu_tournament", data_dict
    else:
        print("\nSaisie non valide\n")
        return "add_players_now", data_dict


def add_players_controller(data_dict):
    """add_players"""
    tournament = data_dict
    player_list_db = Player.list_all()
    player_choose = add_players_view(player_list_db)
    choice = player_choose
    if choice == "b":
        return "menu_tournament"
    player_find = Player.find(player_choose)
    player = player_find[0]
    tournament.add_player(player.serialize())
    if tournament.status == "ready":
        return "load_one_tournament_ready", data_dict

    return "add_players", data_dict


def start_tournament_controller(data_dict):
    """Start tournament"""
    tournament = data_dict
    tournament.start_tournament()
    choice = start_tournament_view(tournament.serialize())
    if choice == "y":
        tournament.update_round()
        return "next_round", data_dict
    elif choice == "n":
        return "menu_tournament", data_dict
    else:
        print("\nSaisie non valide")
        return "start_tournament", data_dict


def next_round_controller(data_dict):
    """"""
