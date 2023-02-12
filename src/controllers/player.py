"""Player controller"""
from src.views.player import menu_player_view, create_player_view, update_player_view, update_player_view_field, \
    delete_player_view, delete_player_view_confirmation, list_all_players_db_view
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
        return "all_players"
    elif choice == "b":
        return "main_menu"
    raise AttributeError("Aucun choix ne correspond")


def create_player_controller():
    """Insert a player in db"""
    player_dict = create_player_view()
    print(player_dict)
    player = Player(**player_dict)
    player_insert_in_db = player.create()
    print(f"{player.last_name} {player.first_name} ajouté à la base de données avec l'id {player.player_id}")
    return "menu_player"


def update_player_controller():
    """Update any fields of a player"""
    player_id = update_player_view()
    player_find = Player.find(player_id)
    player_field_update = update_player_view_field(player_find)
    Player.update(player_field_update[0], player_field_update[1], player_field_update[2])

    return "menu_player"


def delete_player_controller():
    """Delete a player by id"""

    player_id = delete_player_view()
    player_find = Player.find(player_id)
    choice = delete_player_view_confirmation(player_find)

    if choice == "y":
        Player.delete(player_id)
        print(f"Le joueur {player_id} à été supprimé")
    elif choice == 'n':
        return "menu_player"
    return "menu_player"


def list_all_players_controller():
    """list all players"""
    all_players = list_all_players_db_view(Player.list_all())
    print(all_players)


def delete_all_players_db_view():
    pass


def delete_all_players_controller():
    """delete all players"""
    choice = delete_all_players_db_view()

    if choice == "y":
        Player.delete_all()
        print("Tou les joueurs ont été supprimé")
    elif choice == "n":
        return "menu_player"
    else:
        raise AttributeError("Aucun choix ne correspond")
    return "menu_player"


