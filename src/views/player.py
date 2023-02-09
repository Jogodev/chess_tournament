"""player function"""


def menu_player_view():
    """Menu player"""
    title = "-----------------------MENU JOUEUR---------------------------"
    txt = """
            [1] - Ajouter un joueur 
            [2] - Modifier un joueur 
            [3] - Supprimer un joueur 
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

    return {"Nom": {last_name}, "Prénom": {first_name}, "Date de naissance": {birthday}, "Genre": {gender},
            "Score": {score}, "Classement": {rank}}


def update_player_view():
    """"""
    title = "----------MODIFIER UN JOUEUR----------"
    print(title)
    pass


def delete_player_view():
    """"""
    title = "----------SUPPRIMER UN JOUEUR----------"
    print(title)
    pass
