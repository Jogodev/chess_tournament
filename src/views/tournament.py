"""tournament views"""


def menu_tournament_view():
    """"""
    title = "----------MENU TOURNOI----------"
    txt = """ 
    [1] - Créer un nouveau tournoi
    [2] - Charger un tournoi
    [3] - Reprendre un tournoi
    [4] - Rapport d'un tournoi en cours
    [b] - Retour au menu principal
    """

    print(title)
    print(txt)

    choice = input("Faites votre choix : ")
    return choice


def create_tournament_view():
    """"""
    title = "----------CRÉATION TOURNOI----------"
    print(title)

    name = input(
        """
        Nom du tournoi ?
        --> """
    )

    location = input(
        """
        Lieu ?
        --> """
    )

    description = input(
        """
        Commentaire ?
        --> """
    )

    return {"name": name, "location": location, "description": description}


def load_tournaments_view(tournament_list):
    """all tournaments"""
    for tournament in tournament_list:
        print(f"[{tournament['tournament_id']}]", end=" | ")
        print(f"{tournament['name']}", end=" | ")
        print(f"Lieu : {tournament['location']}", end=" | ")
        print(f"{tournament['start_date']}", end=" | ")
        print(f"{tournament['end_date']}", end=" | ")
        print(f"{tournament['id_current_round']}", end=" | ")
        print(f"{tournament['round_list']}", end=" | ")
        print(f"{tournament['description']}", end=" | ")
        if len(tournament['player_list']) == 0:
            print("Aucun joueur ajouté", end="\n")
        elif len(tournament['player_list']) == 1:
            print(f"{len(tournament['player_list'])} joueur ajouté")
        elif len(tournament['player_list']) == 2:
            print(f"{len(tournament['player_list'])} joueurs ajouté tournoi prêt à commencer")
        else:
            print(f"{len(tournament['player_list'])} joueurs ajouté")

    choice = input(
        """
        Quel tournoi voulez-vous charger ?
        --> """
    )

    return choice


def load_one_tournament_ready_view(tournament_dict):
    """one tournament"""
    print("Vous avez chargé ce tournoi : ")
    print(f"{tournament_dict['tournament_id']}", end=" | ")
    print(f"{tournament_dict['name']}", end=" | ")
    print(f"Lieu : {tournament_dict['location']}", end=" | ")
    print(f"{tournament_dict['start_date']}", end=" | ")
    print(f"{tournament_dict['end_date']}", end=" | ")
    print(f"{tournament_dict['id_current_round']}", end=" | ")
    print(f"{tournament_dict['round_list']}", end=" | ")
    print(f"{tournament_dict['description']}", end=" | ")
    print(f"{tournament_dict['player_list']}", end="\n")

    choice = input(
        """
        Commencer le tournoi ?
        y -> [oui] ou n -> [non] 
        --> """
    )
    return choice


def load_one_tournament_view(tournament_dict):
    """one tournament"""
    print("Vous avez chargé ce tournoi : ")
    print(f"{tournament_dict['tournament_id']}", end=" | ")
    print(f"{tournament_dict['name']}", end=" | ")
    print(f"Lieu : {tournament_dict['location']}", end=" | ")
    print(f"{tournament_dict['start_date']}", end=" | ")
    print(f"{tournament_dict['end_date']}", end=" | ")
    print(f"{tournament_dict['id_current_round']}", end=" | ")
    print(f"{tournament_dict['round_list']}", end=" | ")
    print(f"{tournament_dict['description']}", end=" | ")
    if not tournament_dict["player_list"]:
        print("Aucun joueur ajouté", end="\n")

    choice = input(
        """
        Ajouter les joueurs ?
        y -> [oui] ou n -> [non] 
        --> """
    )
    return choice


def add_players_now_view():
    """add players"""

    choice = input(
        """
        Voulez-vous ajouter les joueur maintenant ?
        y -> [oui] ou n -> [non] 
        --> """
    )

    return choice


def add_players_view(player_list_db):
    """add players"""

    for player in player_list_db:
        print(f"[{player['player_id']}]", end=" | ")
        print(f"{player['last_name']} {player['first_name']}", end=" | ")
        print(f"{player['gender']}", end=" | ")
        print(f"Rang : {player['elo']}", end=" | ")
        print(f"Score : {player['score']}")

    player = input(
        """
        Ajouter un joueur 
        --> """
    )

    return player


def load_one_tournament_ready_view(tournament_dict):
    """"""

    print("Vous avez chargé ce tournoi : ")
    print(f"{tournament_dict['tournament_id']}", end=" | ")
    print(f"{tournament_dict['name']}", end=" | ")
    print(f"Lieu : {tournament_dict['location']}", end=" | ")
    print(f"{tournament_dict['start_date']}", end=" | ")
    print(f"{tournament_dict['end_date']}", end=" | ")
    print(f"{tournament_dict['id_current_round']}", end=" | ")
    print(f"{tournament_dict['round_list']}", end=" | ")
    print(f"{tournament_dict['description']}", end=" | ")
    if not tournament_dict["player_list"]:
        print("Aucun joueur ajouté", end="\n")

    choice = input(
        """
        Ce tournoi est prêt voulez vous le commencer ?
        y -> [oui] ou n -> [non] 
        --> """
    )
    return choice
