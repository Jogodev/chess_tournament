"""Reports views"""
from prettytable import PrettyTable


def menu_report_view():
    """Menu of the reports"""
    title = "----------RAPPORTS----------"
    txt = """ 
    [1] - Tous les joueurs
    [2] - Tous les tournois
    [3] - Rapports d'un tournoi  
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
    table.field_names = ["ID", "Nom", "Lieu", "Débuté le", "Fini le", "Commentaire"]
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


def one_tournament_choice_view(tournaments):
    """View of on tournament"""
    for tournament in tournaments:
        print(f"[{tournament['tournament_id']}]", end=" | ")
        print(f"{tournament['name']}")

    choice = input(
        """
        De quel tournoi voulez-vous les rapports ?
        --> """
    )

    return choice


def report_choice_view(tournament):
    """Choice between some reports"""
    table = PrettyTable()
    table.clear()
    table.field_names = ["ID", "Nom", "Débuté le", "Fini le", "Commentaire"]
    table.add_row([
        tournament["tournament_id"],
        tournament["name"],
        tournament["start_date"],
        tournament["end_date"],
        tournament["description"],
    ])
    print(table)
    choice = input(
        """
        Quel rapport voulez-vous consultez ?
        [1] - Joueurs par ordre alphabétiques
        [2] - Rondes et matchs
        [b] - Retour au menu 
        --> """
    )
    return choice

def players_in_tournament_view(tournament):
    """players in tournament sort by last name"""
    pass


def rounds_and_games_tournament_view():
    """view of rounds and games of a tournament"""
    pass
