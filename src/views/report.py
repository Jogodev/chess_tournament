"""Reports views"""
from prettytable import PrettyTable


def menu_report_view():
    """Menu of the reports"""
    title = "----------RAPPORTS----------"
    txt = """ 
    [1] - Tous les joueurs
    [2] - Tous les tournois
    [3] - Nom et dates d'un tournoi
    [4] - Joueurs d'un tournoi
    [5] - 
    [b] - Retour au menu principal
    """

    print(title)
    print(txt)
    choice = input("Faites votre choix : ")
    return choice


def all_players_view(sort_players):
    """Player sort by last name"""
    print("----------TOUT LES JOUEURS----------")
    table = PrettyTable()
    table.field_names = ["ID", "Nom", "Prénom", "Gender", "Date de naissance"]
    for player in sort_players:
        table.add_row([
            player["player_id"],
            player["last_name"],
            player["first_name"],
            player["gender"],
            player["birthday"]
        ])
    print(table)

    choice = input(
        """
    [b] retour aux choix des rapports
    --> """
    )
    return choice


def all_tournaments_view(tournaments):
    """all tournaments in database"""
    print("----------TOUT LES TOURNOIS----------")
    table = PrettyTable()
    table.field_names = ["ID", "Nom", "Lieu", "Date de début", "Date de fin", "Description"]
    for tournament in tournaments:
        table.add_row([
            tournament["tournament_id"],
            tournament["name"],
            tournament["location"],
            tournament["start_date"],
            tournament["end_date"],
            tournament["description"],
        ])
    print(table)
    choice = input(
        """
    [b] retour aux choix des rapports
    --> """
    )
    return choice


def one_tournament_report_view():
    """View of on tournament"""
    pass


def players_in_tournament_view(tournament):
    """players in tournament sort by last name"""
    pass


def rounds_and_games_tournament_view():
    """view of rounds and games of a tournament"""
    pass
