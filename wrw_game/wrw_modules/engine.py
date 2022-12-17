"""Engine module provides two functions:
get_player_name and play."""

from wrw_modules import exceptions
from wrw_modules import models
from wrw_modules import settings


def get_player_name():
    """
    This function asks the user to type in his or her name and return it back.
    Leading and trailing whitespaces are to be trimmed..
    :return: user's name as a string. Name contains at least one character.
    """

    name = ""
    while not name:
        name = input("HI! WHAT'S YOUR NAME?: ").strip()
    return name


def play():
    """
    This function initializes player and enemy instances.
    It processes game rounds inside of an endless loop stage by stage.
    If an enemy is defeated - a new one is initialized with level increased
    by 1 (one). This case is reported to the terminal.
    If a player is defeated - the "Game Over" message is reported to the
    terminal.
    """

    player_name = get_player_name()
    player = models.Player(player_name)
    enemy = models.Enemy(settings.LEVEL)

    while True:
        print("FIGHT!")
        try:
            player.attack(enemy)
            player.defense(enemy)
        except exceptions.EnemyDown as msg:
            print(msg)
            enemy = models.Enemy(enemy.level + 1)
