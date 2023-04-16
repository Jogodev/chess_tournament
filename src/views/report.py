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
    print("\n----------TOUT LES JOUEURS----------")
    table = PrettyTable()
    table.field_names = ["ID", "Nom", "Prénom", "Sexe", "Date de naissance"]
    for player in sort_players:
        table.add_row([
            player["player_id"],
            player["last_name"],
            player["first_name"],
            player["gender"],
            player["birthday"]
        ])
    print(f"\n{table}\n")
    choice = input(
        """
    [b] retour aux choix des rapports
    --> """
    )
    return choice


def all_tournaments_view(tournaments):
    """all tournaments in database"""
    print("\n----------TOUT LES TOURNOIS----------")
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
    print(f"\n{table}\n")
    choice = input(
        """
    [b] retour aux choix des rapports
    --> """
    )
    return choice


def one_tournament_choice_view(tournaments):
    """View of on tournament"""
    print("\n----------TOURNOIS----------")
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
    print("\n----------RAPPORT D'UN TOURNOI----------")
    table = PrettyTable()
    table.field_names = ["ID", "Nom", "Débuté le", "Fini le", "Commentaire"]
    table.add_row([
        tournament["tournament_id"],
        tournament["name"],
        tournament["start_date"],
        tournament["end_date"],
        tournament["description"],
    ])
    print(f"\n{table}\n")
    choice = input(
        """
        Quel rapport voulez-vous consultez ?
        [1] - Joueurs par ordre alphabétiques
        [2] - Rondes et matchs
        [b] - Retour au menu 
        --> """
    )

    return choice


def players_in_tournament_view(players):
    """players in tournament sort by last name"""
    print("\n----------JOUEURS DU TOURNOI----------")
    table = PrettyTable()
    table.field_names = ["ID", "Nom", "Prénom", "Date de naissance", "Sexe"]
    for player in players:
        table.add_row([
            player["player_id"],
            player["last_name"],
            player["first_name"],
            player["gender"],
            player["birthday"]
        ])
    print(f"\n{table}\n")

    choice = input(
        """
        [b] retour aux choix du tournoi
        --> """
    )

    return choice


def rounds_and_games_tournament_view(rounds, results, players):
    """view of rounds and games of a tournament"""
    print("\n----------RONDES ET MATCHS DU TOURNOI----------")
    table = PrettyTable()
    table.field_names = ["ID", "Nom", "Commencé le", "Fini le", "Matchs"]
    for current_round in rounds:
        table.add_row([
            current_round["round_id"],
            current_round["round_name"],
            current_round["start_datetime"],
            current_round["end_datetime"],
            current_round["game_list"],
        ])

    result_table = PrettyTable()
    result_table.field_names = ["Joueur", "Score"]
    for player in players.items():
        result_table.add_row([
            player[0],
            player[1],
        ])
    print(f"\n{table}\n")
    print("\n----------Résultats----------\n")
    print(f"\n{result_table}\n")
    choice = input(
        """
        [b] retour aux choix du tournoi
        --> """
    )

    return choice
