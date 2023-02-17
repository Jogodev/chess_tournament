"""Player controller"""
from src.views.player import (
    menu_player_view,
    create_player_view,
    update_player_view,
    update_player_view_field,
    delete_player_view,
    delete_player_view_confirmation,
    list_all_players_db_view,
    delete_all_players_db_view,
    players_db_test_view
)
from src.models.player import Player


def menu_player_controller():
    """"""
    choice = menu_player_view()

    if choice == "1":
        return "create_player"
    elif choice == "2":
        return "update_player"
    elif choice == "3":
        return "delete_player"
    elif choice == "4":
        return "list_all_players"
    elif choice == "5":
        return "delete_all_players"
    elif choice == "6":
        return "create_test_db"
    elif choice == "b":
        return "main_menu"
    raise ValueError("Aucun choix ne correspond")


def create_player_controller():
    """Insert a player in db"""
    player_dict = create_player_view()
    print(player_dict)
    player = Player(**player_dict)
    player_insert_in_db = player.create()
    print(
        f"{player.last_name} {player.first_name} ajouté à la base de données avec l'id {player.player_id}"
    )
    return "menu_player"


def update_player_controller():
    """Update any fields of a player"""
    player_id = update_player_view()
    player_list = Player.find(player_id)
    assert len(player_list) == 1
    player = player_list[0]
    player_field_update = update_player_view_field(player.serialize())
    player.update(player_field_update)

    return "menu_player"


def delete_player_controller():
    """Delete a player by id"""

    player_id = delete_player_view()
    player_list = Player.find(player_id)
    assert len(player_list) == 1
    player = player_list[0]
    choice = delete_player_view_confirmation(player.serialize())

    if choice == "y":
        player.delete()
    elif choice == "n":
        return "menu_player"
    return "menu_player"


def list_all_players_controller():
    """list all players"""
    all_players = Player.list_all()
    choice = list_all_players_db_view(all_players)

    if choice == "b":
        return "menu_player"
    elif choice == "m":
        return "main_menu"
    else:
        raise ValueError("Aucun choix ne correspond")


def delete_all_players_controller():
    """delete all players"""
    choice = delete_all_players_db_view()

    if choice == "y":
        Player.delete_all()
    elif choice == "n":
        return "menu_player"
    else:
        raise ValueError("Aucun choix ne correspond")
    return "menu_player"


def players_db_test_controller():
    """Create a test db of 8 players"""
    choice = players_db_test_view()

    if choice == "y":
        Player.boot()
    elif choice == "b":
        return "menu_player"
    elif choice == "m":
        return "main_menu"
    else:
        raise ValueError("Aucun choix ne correspond")
    return "menu_player"
