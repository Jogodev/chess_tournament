class Tournament:
    def __init__(
            self,
            name,
            location,
            start_date,
            end_date,
            id_current_round,
            round_list,
            player_list,
            description,
            round_number=4
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.id_current_round = id_current_round
        self.round_list = round_list
        self.player_list = player_list
        self.description = description
        self.round_number = round_number



