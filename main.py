"""Main"""

from src.controllers.main import main_menu_controller
from src.controllers.player import menu_player_controller, create_player_controller, update_player_controller, \
    delete_player_controller, list_all_players_controller, delete_all_players_controller, players_db_test_controller
from src.controllers.report import all_players_report_controller, menu_report_controller, \
    all_tournaments_report_controller, players_in_tournament_controller, one_tournament_report_controller, \
    rounds_and_games_tournament_controller
from src.controllers.tournament import menu_tournament_controller, create_tournament_controller, \
    load_tournaments_controller, add_players_controller, load_one_tournament_controller, \
    start_tournament_controller, load_one_tournament_ready_controller, end_round_controller, \
    end_tournament_controller, get_scores_controller, next_round_controller

controller_dict = {
    # Main menu
    "main_menu": main_menu_controller,
    # player
    "menu_player": menu_player_controller,
    "create_player": create_player_controller,
    "update_player": update_player_controller,
    "delete_player": delete_player_controller,
    "list_all_players": list_all_players_controller,
    "delete_all_players": delete_all_players_controller,
    "create_test_db": players_db_test_controller,
    # Tournament
    "menu_tournament": menu_tournament_controller,
    "create_tournament": create_tournament_controller,
    "load_tournaments": load_tournaments_controller,
    "load_one_tournament": load_one_tournament_controller,
    "load_one_tournament_ready": load_one_tournament_ready_controller,
    "add_players": add_players_controller,
    "start_tournament": start_tournament_controller,
    "get_scores": get_scores_controller,
    "end_round": end_round_controller,
    "next_round": next_round_controller,
    "end_tournament": end_tournament_controller,
    # Reports
    "menu_report": menu_report_controller,
    "all_players_report": all_players_report_controller,
    "all_tournaments_report": all_tournaments_report_controller,
    "players_in_tournament": players_in_tournament_controller,
    "one_tournament_report": one_tournament_report_controller,
    "rounds_and_games": rounds_and_games_tournament_controller,
}


def main():
    """Program start"""
    data_dict = dict()
    string_controller, data_dict = main_menu_controller(data_dict)

    while True:
        controller = controller_dict[string_controller]
        string_controller, data_dict = controller(data_dict)


if __name__ == "__main__":
    main()
