"""Tournament controller"""

from src.views.tournament import menu_tournament_view, create_tournament_view, add_players_now_view, \
    load_tournaments_view, add_players_view
from src.models.tournament import Tournament
from src.models.player import Player


def menu_tournament_controller():
    """Menu tournament controller"""
    choice = menu_tournament_view()

    if choice == "1":
        return "create_tournament"
    elif choice == "2":
        return "load_tournament"
    elif choice == "2":
        return "add_players_now"
    elif choice == "b":
        return "main_menu"
    else:
        raise ValueError("Aucun choix ne correspond")


def create_tournament_controller():
    """Create a controller"""
    tournament_dict = create_tournament_view()
    tournament = Tournament(**tournament_dict)
    tournament_insert_in_db = tournament.save_tournament()

    return "add_players_now"


def add_players_now_controller():
    """add players"""
    choice = add_players_now_view()

    if choice == "y":
        return "add_players"
    elif choice == "n":
        return "tournament_menu"
    else:
        print('\nSaisie non valide')

    return choice


def add_players_controller():
    """add_players"""
    return add_players_view()


def load_tournaments_controller():
    """Load a tournament """
    return load_tournaments_view()