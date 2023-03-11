import logging, secrets, datetime

import pytest

from src.models.round import Round


def test_init_round():
    """ """

    round = Round(tournament_id=secrets.token_hex(2), round_name=secrets.token_hex(2))

    print(round)


def test_create_round():
    """ """

    round = Round(tournament_id=secrets.token_hex(2), round_name=secrets.token_hex(2))

    print(round)

    round.create()
