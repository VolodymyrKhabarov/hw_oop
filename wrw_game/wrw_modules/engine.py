"""Engine module provides two functions:
get_player_name and play."""

from . import exceptions
from . import models
from . import settings


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
    ``KeyboardInterrupt`` is handled as well - it's behavior is similar
    to "Game Over" event, but "game over" message is omitted.
    """

    player_name = get_player_name()
    player = models.Player(player_name)
    enemy = models.Enemy(settings.LEVEL)

    while True:
        print("FIGHT!")
        try:
            player_move = player.select_attack()
            bot_move = enemy.select_defence()
            player.attack(enemy, player_move, bot_move)

            player_move = player.select_defence()
            bot_move = enemy.select_attack()
            player.defence(player_move, bot_move)
        except exceptions.GameOver:
            print(f'{player.name} is defeated!')
            print(f'SCORE POINTS: {player.score}')
            print('GAME OVER!')
            with open('scores.txt', 'a', encoding='utf-8') as file:
                file.write(f'Name: {player.name}, score: {player.score}\n')
            break
        except exceptions.EnemyDown:
            print(f'Enemy level {enemy.level} is defeated!')
            player.score += settings.REWARD
            enemy = models.Enemy(enemy.level + 1)
            print(f"FIGHT AGAINST THE ENEMY LEVEL {enemy.level}!")
