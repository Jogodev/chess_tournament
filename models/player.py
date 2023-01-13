class Player:
    def __init__(
            self,
            id: str,
            lastname: str,
            firstname: str,
            birthday: str,
    ):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday

    def add_player(self):
        input("ajouter un joueur")

    def remove_player(self):
        pass


