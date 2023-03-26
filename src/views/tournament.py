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
        if not tournament["start_date"]:
            print("Pas commencé", end=" | ")
        else:
            print(f"Commencé le : {tournament['start_date']}", end=" | ")
        if not tournament['end_date']:
            print("", end=" | ")
        else:
            print(f"{tournament['end_date']}", end=" | ")
        print(f"Ronde actuelle : {tournament['id_current_round']}", end=" | ")
        print(f"Rondes prévues : {tournament['total_rounds']}", end=" | ")
        print(f"{tournament['description']}", end=" | ")
        if len(tournament["player_list"]) == 0:
            print("Aucun joueur ajouté", end="\n")
        elif len(tournament["player_list"]) == 1:
            print(f"{len(tournament['player_list'])} joueur ajouté")
        elif len(tournament["player_list"]) == 8:
            print(
                f"{len(tournament['player_list'])} joueurs ajouté tournoi prêt à commencer"
            )
        else:
            print(f"{len(tournament['player_list'])} joueurs ajouté")

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
    print(f"Lieu : {tournament_dict['location']}", end=" | ")
    if not tournament_dict["start_date"]:
        print("Pas commencé", end=" | ")
    else:
        print(f"Commencé le : {tournament_dict['start_date']}", end=" | ")
    print(f"Terminé le{tournament_dict['end_date']}", end=" | ")
    print(f"Ronde actuelle : {tournament_dict['id_current_round']}", end=" | ")
    print(f"Rondes prévues : {tournament_dict['total_rounds']}", end=" | ")
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
        b --> [retour au menu principal]
        --> """
    )

    return player


def load_one_tournament_ready_view(tournament_dict):
    """one tournament status ready"""
    print("\nVous avez chargé ce tournoi : ", end="\n")
    print(f"{tournament_dict['tournament_id']}", end=" | ")
    print(f"{tournament_dict['name']}", end=" | ")
    print(f"Lieu : {tournament_dict['location']}", end=" | ")
    if not tournament_dict["start_date"]:
        print("Pas commencé", end=" | ")
    else:
        print(f"Commencé le : {tournament_dict['start_date']}", end=" | ")
    print(f"{tournament_dict['end_date']}", end=" | ")
    print(f"Ronde actuelle : {tournament_dict['id_current_round']}", end=" | ")
    print(f"Id ronde : {tournament_dict['round_list']}", end=" | ")
    print(f"Rondes prévues : {tournament_dict['total_rounds']}", end=" | ")
    print(f"{tournament_dict['description']}", end=" | ")
    print(f"{tournament_dict['player_list']}", end="\n")

    choice = input(
        """
        Ce tournoi est prêt voulez-vous commencer la 1ère ronde?
        y -> [oui] ou n -> [non] 
        --> """
    )
    return choice


def start_tournament_view(tournament):
    """"""
    print(f"Ronde N°{tournament['id_current_round']} du tournoi {tournament['name']}")

    choice = input(
        """
        Entrer les scores des matchs ?
        y -> [oui] ou n -> [non] 
        --> """
    )

    return choice


def get_scores_view(current_round):
    """Get the scores of all games"""
    print("Entrer les scores des différents match avant de passé à la ronde suivante")
    print(f"Match 1 : {current_round['game_list'][0]}")
    print("")
    print(f"Match 2 : {current_round['game_list'][1]}")
    print("")
    print(f"Match 3 : {current_round['game_list'][2]}")
    print("")
    print(f"Match 4 : {current_round['game_list'][3]}")
    print("")
    print("1 = Victoire du joueur 1")
    print("2 = Victoire du joueur 2")
    print("3 = Match nul")
    player_id_1 = current_round['game_list'][0][0][0]
    player_id_2 = current_round['game_list'][0][1][0]

    game_1 = input(
        """  
        Match 1    
        --> """
    )

    game_2 = input(
        """  
        Match 2    
        --> """
    )

    game_3 = input(
        """  
        Match 3    
        --> """
    )

    game_4 = input(
        """  
        Match 4    
        --> """
    )

    if game_1 == "1":
        game_1 = [(player_id_1, 1), (player_id_2, 0)]

    elif game_1 == "2":
        game_1 = [(player_id_1, 0), (player_id_2, 1)]

    elif game_1 == "3":
        game_1 = [(player_id_1, 0.5), (player_id_2, 0.5)]

    if game_2 == "1":
        game_2 = [(player_id_1, 1), (player_id_2, 0)]

    elif game_2 == "2":
        game_2 = [(player_id_1, 0), (player_id_2, 1)]

    elif game_2 == "3":
        game_2 = [(player_id_1, 0.5), (player_id_2, 0.5)]

    if game_3 == "1":
        game_3 = [(player_id_1, 1), (player_id_2, 0)]

    elif game_3 == "2":
        game_3 = [(player_id_1, 0), (player_id_2, 1)]

    elif game_3 == "3":
        game_3 = [(player_id_1, 0.5), (player_id_2, 0.5)]

    if game_4 == "1":
        game_4 = [(player_id_1, 1), (player_id_2, 0)]

    elif game_4 == "2":
        game_4 = [(player_id_1, 0), (player_id_2, 1)]

    elif game_4 == "3":
        game_4 = [(player_id_1, 0.5), (player_id_2, 0.5)]

    return [game_1, game_2, game_3, game_4]


def next_round_view():
    """all rounds after the first round"""
    choice = input(
        f"""
        Voulez-vous lancer la 2ème ronde de ce tournoi ?
        y -> [oui] ou n -> [non] 
        --> """
    )
    return choice


def end_tournament_view():
    """End of the tournament"""
    print("Fin du tournoi")
