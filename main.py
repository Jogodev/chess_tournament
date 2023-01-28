from src.models.tournament import Tournament
from src.models.player import Player
from src.models.round import Ronde
from src.models.game import Game
import itertools
import json

def main():
    player1 = Player('Glass')
    player1.create()

    player1.update()


if __name__ == "__main__":
        main()
