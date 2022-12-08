"""
Exceptions module provide GameOver and EnemyDown exceptions.
"""


class GameOver(Exception):
    """
    This is an exceptional scenario when player is defeated.
    A custom exception ``GameOver`` is used to track these cases.
    Exception provides the details on the player's instance: its score points.
    """


class EnemyDown(Exception):
    """
    This is an exceptional scenario when enemy is defeated.
    A custom exception EnemyDown is used to track these cases.
    Exception provides the details on the enemy's instance: its level.
    """
