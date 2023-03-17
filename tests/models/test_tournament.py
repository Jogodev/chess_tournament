import pytest
import secrets
import logging

from src.models.tournament import Tournament
from src.models.player import Player


def test_init_tournament():

    name = secrets.token_hex(2)
    t = Tournament(name)


def test_create_tournament():

    name = secrets.token_hex(2)
    t = Tournament(name)
    t.create()


def test_add_player():

    # n player
    n = 2

    # init 2 fale plaue
    p_list = [Player(player_id=secrets.token_hex(2)) for _ in range(n)]
    assert len(p_list) == n

    # created in db
    _ = [p.create() for p in p_list]

    # init tour
    t = Tournament(secrets.token_hex(2))
    t.create()
    print(t.__dict__)

    for p in p_list:
        t.add_player(p.__dict__)

    # t.update()
