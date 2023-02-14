"""player function"""


def menu_player_view():
    """Menu player"""
    title = "-----------------------MENU JOUEUR---------------------------"
    txt = """
            [1] - Ajouter un joueur 
            [2] - Modifier un joueur 
            [3] - Supprimer un joueur 
            [4] - Liste de tous les joueurs
            [5] - Supprimer tous les joueurs
            [b] - retour au menu principal
            """
    print(title)
    print(txt)

    choice = input("Faites votre choix : ")
    return choice


def create_player_view():
    """Menu create player"""
    title = "----------CRÉER UN JOUEUR----------"
    print(title)

    last_name = input(
        """
         Nom ? 
        --> """
    )

    first_name = input(
        """
         Prénom ? 
        --> """
    )

    birthday = input(
        """
         Date de naissance ? 
        --> """
    )

    gender = input(
        """
         Sexe ? 
        --> """
    )

    score = input(
        """
         Score ? 
        --> """
    )

    rank = input(
        """
         Classement ? 
        --> """
    )

    return {
        "last_name": last_name,
        "first_name": first_name,
        "birthday": birthday,
        "gender": gender,
        "score": score,
        "rank": rank,
    }


def update_player_view():
    """update player view"""
    title = "----------MODIFIER UN JOUEUR----------"
    print(title)

    player_id = input(
        """
        Id du joueur à modifier ?
        --> """
    )

    return player_id


def update_player_view_field(player_find):  # mettre p_dict à la place
    """Update player view"""
    title = "----------MODIFIER UN JOUEUR----------"
    print(title)
    print(f"Vous allez modifier ce joueur : {player_find}")

    # comme on recoit un dict ==> ON peut suppr le [0]
    player_id = player_find[0]["player_id"]

    key = input(
        """
        Champ à modifier ?
        --> """
    )

    value = input(
        """
        Nouvelle valeur ?
        --> """
    )

    return [key, value, player_id]


def delete_player_view():
    """delete player view"""
    title = "----------SUPPRIMER UN JOUEUR----------"
    print(title)

    player_id = input(
        """
        Id du joueur à supprimer
        --> """
    )

    return player_id


def delete_player_view_confirmation(player_find):
    """Delete player view confirmation"""
    title = "----------SUPPRIMER UN JOUEUR----------"
    print(title)
    print(f"Vous allez supprimer ce joueur : {player_find}")

    choice = input(
        """
        Êtes-vous sûre ?
        y -> [oui] ou n -> [non]
        --> """
    )

    return choice


def list_all_players_db_view(all_players):
    """all players"""
    print("----------LISTE DE TOUT LES JOUEURS----------")
    print(all_players)


def delete_all_players_db_view():
    print(
        "Vous avez la possibilité de supprimer tout les joueurs"
        "!!!ATTENTION CETTE ACTION EST IRRÉVERSIBLE!!!"
    )
    choice = input(
        """
        Voulez-vous supprimer la base de données ?
        y -> [oui] ou n -> [non] 
        --> """
    )

    return choice
