"""tournament views"""


def menu_tournament_view():
    """"""
    title = "----------MENU TOURNOI----------"
    txt = """ 
    [1] - Créer un nouveau tournoi
    [2] - Charger un tournoi
    [3] - Rapport d'un tournoi en cours
    [b] - Retour au menu principal
    --> """

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
    """"""
    # [Tournament(**tournament) for tournament in tournament_list]
    for tournament in tournament_list:
        print(f"{tournament['tournament_id']}", end=" | ")
        print(f"{tournament['name']}", end=" | ")
        print(f"{tournament['location']}", end=" | ")
        print(f"{tournament['start_date']}", end=" | ")
        print(f"{tournament['end_date']}", end=" | ")
        print(f"{tournament['id_current_round']}", end=" | ")
        print(f"{tournament['round_list']}", end=" | ")
        print(f"{tournament['description']}", end=" | ")
        if tournament["player_list"] == []:
            print("Aucun joueur ajouté", end="\n")

    choice = input(
        """
        Quel tournoi voulez-vous charger ?
       --> """
    )

    return choice


def load_one_tournament_view(tournament_dict):
    """one tournament"""
    print("Vous avez chargé ce tournoi : ")
    print(f"{tournament_dict['tournament_id']}", end=" | ")
    print(f"{tournament_dict['name']}", end=" | ")
    print(f"{tournament_dict['location']}", end=" | ")
    print(f"{tournament_dict['start_date']}", end=" | ")
    print(f"{tournament_dict['end_date']}", end=" | ")
    print(f"{tournament_dict['id_current_round']}", end=" | ")
    print(f"{tournament_dict['round_list']}", end=" | ")
    print(f"{tournament_dict['description']}", end=" | ")
        if tournament_dict["player_list"] == []:
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


def add_players_view():
    """add players"""

    for player in player_list:
        print(f"{player['player_id']}")
        print(f"{player['last_name']}", end=" | ")
        print(f"{player['first_name']}", end=" | ")
        print(f"{player['gender']}", end=" | ")
        print(f"{player['rank']}", end=" | ")
        print(f"{player['score']}")

    player_1 = input(
        """
        Ajouter le joueur 1
        --> """
    )

    player_2 = input(
        """
        Ajouter le joueur 2
        --> """
    )

    player_3 = input(
        """
        Ajouter le joueur 3
        --> """
    )

    player_4 = input(
        """
        Ajouter le joueur 4
        --> """
    )

    player_5 = input(
        """
        Ajouter le joueur 5
        --> """
    )

    player_6 = input(
        """
        Ajouter le joueur 6
        --> """
    )

    player_7 = input(
        """
        Ajouter le joueur 7
        --> """
    )

    player_8 = input(
        """
        Ajouter le joueur 8
        --> """
    )

    return {
        player_1,
        player_2,
        player_3,
        player_4,
        player_5,
        player_6,
        player_7,
        player_8,
    }
