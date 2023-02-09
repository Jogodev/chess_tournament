"""Tournament controller"""
from src.views.tournament import menu_tournament_view, create_tournament_view, update_tournament_view
from src.models.tournament import Tournament


def menu_tournament_controller():
    """"""
    choice = menu_tournament_view()

    if choice == "1":
        return "create_tournament"
    elif choice == "2":
        return "update_tournament"
    elif choice == "b":
        return "main_menu"
    # else:
    #     raise AttributeError("Aucun choix ne correspond")


def create_tournament_controller():
    """"""
    tournament = create_tournament_view()
    print(tournament)
    return "tournament_menu"


def update_tournament_controller():
    """"""
    tournament = update_tournament_view()
    print(tournament)
    return "tournament_menu"
