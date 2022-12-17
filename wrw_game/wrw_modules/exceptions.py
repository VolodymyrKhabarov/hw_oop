"""
Exceptions module provide GameOver and EnemyDown exceptions.
"""


class GameOver(Exception):
    """
    This is an exceptional scenario when player is defeated.
    A custom exception ``GameOver`` is used to track these cases.
    Exception provides the details on the player's instance: its score points.
    """

    def __init__(self, player):
        self.player = player

    def __str__(self):
        return f'{self.player.name} is defeated! GAME OVER! SCORE POINTS: {self.player.score}'


class EnemyDown(Exception):
    """
    This is an exceptional scenario when enemy is defeated.
    A custom exception EnemyDown is used to track these cases.
    Exception provides the details on the enemy's instance: its level.
    """

    def __init__(self, level):
        self.level = level

    def __str__(self):
        return f'Enemy level {self.level} is defeated!'
