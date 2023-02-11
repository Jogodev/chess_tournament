"""Player controller"""
from src.views.player import menu_player_view, create_player_view, update_player_view, update_player_view_field, delete_player_view, delete_player_view_confirmation
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
    elif choice == "b":
        return "main_menu"
    raise AttributeError("Aucun choix ne correspond")


def create_player_controller():
    """"""
    player_dict = create_player_view()
    print(player_dict)
    player = Player(**player_dict)
    player_insert_in_db = player.create()
    print(f"{player.last_name} {player.first_name} ajouté à la base de données avec l'id {player.player_id}")
    return "menu_player"


def update_player_controller():
    """"""
    player_id = update_player_view()
    player_find = Player.find(player_id)
    player_field_update = update_player_view_field(player_find)
    Player.update(player_field_update[0], player_field_update[1], player_field_update[2])

    return "menu_player"


def delete_player_controller():
    """"""

    player_id = delete_player_view_confirmation()
    player_find = Player.find(player_id)


    Player.delete(player_id)
    return "menu_player"



