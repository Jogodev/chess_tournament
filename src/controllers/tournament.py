"""Tournament controller"""

from src.views.tournament import menu_tournament_view, create_tournament_view, add_players_now_view, \
    load_tournaments_view, add_players_view, load_one_tournament_view
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
        raise ValueError("Aucun choix ne correspond")


def create_tournament_controller(data_dict):
    """Create a controller"""
    tournament_dict = create_tournament_view()
    tournament = Tournament(**tournament_dict)
    tournament_insert_in_db = tournament.save_tournament()

    return "add_players_now", data_dict


def load_tournaments_controller(data_dict):
    """Load all tournaments """
    tournament_list = Tournament.load_tournaments()
    #transform tournament_list en dict;
    tournament_id = load_tournaments_view(tournament_list)
    #tournament_find = Tournament.find(tournament_id)
    data_dict["tournament_id"] = tournament_id

    return "load_one_tournament", data_dict


def load_one_tournament_controller(data_dict):
    """Load one tournament"""
    tournament_id = data_dict["tournament_id"]
    tournament_list = Tournament.find(tournament_id)
    tournament = tournament_list[0]
    choice = load_one_tournament_view(tournament.serialize())
    data_dict = tournament

    if choice == "y":
        return "add_players", data_dict
    elif choice == "n":
        return "tournament_menu", data_dict
    else:
        print("Aucun choix ne correspond")

    return "add_players", data_dict


def add_players_now_controller(data_dict):
    """add players"""
    choice = add_players_now_view()

    if choice == "y":
        return "add_players", data_dict
    elif choice == "n":
        return "tournament_menu", data_dict
    else:
        print('Saisie non valide')

    return choice, data_dict


def add_players_controller(data_dict):
    """add_players"""
    player_list = Player.list_all()
    print(player_list)
    player = add_players_view(player_list)
    player_list.append(player)


    if len(player) > 8:
        return "add_player"
    else:
        print("les 8 joueurs ont été ajouté, que le tournoi commence !!! ")

    return "tournament_menu", data_dict