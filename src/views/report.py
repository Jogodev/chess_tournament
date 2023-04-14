"""Reports views"""


def menu_report_view():
    """"""
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
    print(sort_players)
    for player in sort_players:
    print(f"{player['last_name']} {player['first_name']}", end=" | ")
    print(f"{player['gender']}", end=" | ")
    print(f"Rang : {player['elo']}", end=" | ")
    print(f"Score : {player['score']}")
    """
    [b] retour aux choix des rapports
    --> """

def all_tournaments_view():
    """all tournaments in database"""