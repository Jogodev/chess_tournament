"""menu function"""


def main_menu_view():
    """Main menu"""

    title = "----------BIENVENUE AU TOURNOI D'ECHECS----------"
    txt = """
         1 - Joueur 
         2 - Tournoi
        """
    print(title)
    print(txt)
    choice = input("Faites votre choix : ")
    return choice
