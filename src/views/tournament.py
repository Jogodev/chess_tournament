"""tournament views"""


def menu_tournament_view():
    """"""
    title = "----------MENU TOURNOI----------"
    txt = """ 
    [1] - Créer un nouveau tournoi
    [2] - Rapport d'un tournoi en cours
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
        Nom du tournoi ?
        --> """
    )

    # name = input(
    #     """
    #     Nom du tournoi ?
    #     --> """
    # )
    #
    # name = input(
    #     """
    #     Nom du tournoi ?
    #     --> """
    # )
    #
    # name = input(
    #     """
    #     Nom du tournoi ?
    #     --> """
    # )


def update_tournament_view():
    """"""
    pass
