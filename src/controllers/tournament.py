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
        print('Saisie non valide')

    return choice


def add_players_controller(tournament):
    """add_players"""
    tournament = Tournament(**tournament)
    player = add_players_view()
    player_list = tournament['player_list']
    player_list.append(player)

    if len(player) > 8:
        return "add_player"
    else:
        print("les 8 joueurs ont été ajouté, que le tournoi commence !!! ")


def load_tournaments_controller():
    """Load all tournaments """
    return load_tournaments_view()


def load_one_tournament_controller():
    """Load one tournament"""
    tournament_id = load_tournaments_view()
    tournament_find = Tournament.find(tournament_id)
    print(tournament_find)

