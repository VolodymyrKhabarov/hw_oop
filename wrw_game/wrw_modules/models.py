"""
This module implements Enemy and Player classes.
The enemy model represents the playing enemy-bot.
All choices made by this model are random.
Player model is controlled by the user.
It represents a playing user.
All choices are controlled by the user.
"""
import random

from . import exceptions
from . import settings


class Enemy:
    """
    Enemy class implementation
    """

    def __init__(self, level: int):
        """
        Initialize an enemy instance
        """

        self.level = level
        self.health = level

    def decrease_health(self):
        """
        Method decreases the health points value by 1 (one).
        If this value becomes less that 1 (one)
        the EnemyDown exception is raised.
        """

        self.health -= 1
        if self.health < 1:
            raise exceptions.EnemyDown
        return self.health

    def select_attack(self):
        """
        Return a random attack choice from valid choices.
        """

        bot_choice = random.choice(settings.CHOICES)
        return bot_choice

    def select_defence(self):
        """
        Return a random defence choice from valid choices.
        """

        bot_choice = random.choice(settings.CHOICES)
        return bot_choice

    def __repr__(self) -> str:
        """
        Implement a human readable string representation for Enemy class
        """

        return self.level

    def __str__(self) -> str:
        """
        Implement type-casting for Enemy. Enemy cast to string type equals to its level
        """

        return self.level


class Player:
    """
    Player class implementation
    """

    def __init__(self, name: str):
        """
        Initialize an player instance
        """

        self.name = name
        self.score = 0
        self.health = settings.PLAYER_HEALTH

    def decrease_health(self):
        """
        Method decreases the health points value by 1 (one).
        If this value becomes less that 1 (one)
        the GameOver exception is raised.
        """

        self.health -= 1
        if self.health < 1:
            raise exceptions.GameOver
        return self.health

    def select_attack(self):
        """
        Return a fight choice made by the user. Performs choice validation.
        """

        while True:
            print('MAKE AN ATTACK CHOICE FROM (WARRIOR - 1, ROBBER - 2, WIZARD - 3): ')
            player_move = input()
            if player_move in ('1', '2', '3'):
                player_choice = settings.CHOICES[int(player_move) - 1]
                return player_choice

    def select_defence(self):
        """
        Return a fight choice made by the user. Performs choice validation.
        """

        while True:
            print('MAKE A DEFENCE CHOICE FROM (WARRIOR - 1, ROBBER - 2, WIZARD - 3): ')
            player_move = input()
            if player_move in ('1', '2', '3'):
                player_choice = settings.CHOICES[int(player_move) - 1]
                return player_choice

    @staticmethod
    def fight(player_move, bot_move):
        """
        Static method to perform a fight.
        Takes two arguments representing attack and defence choices.
        Performs fight result calculation and return it back.
        """

        if player_move == bot_move:
            return "draw"
        battle = (player_move, bot_move)
        if battle in settings.WIN_CONDITION:
            return True
        return False

    def attack(self, enemy, player_move, bot_move):
        """
        Perform attack on an enemy instance.
        """

        result = self.fight(player_move, bot_move)
        if result == 'draw':
            print("IT'S A DRAW!")
        elif result:
            enemy.decrease_health()
            self.score += 1
            print("YOUR ATTACK IS SUCCESSFUL!")
        else:
            print("YOUR ATTACK IS FAILED!")

    def defence(self, player_move, bot_move):
        """
        Perform defence from an enemy attack.
        """

        result = self.fight(player_move, bot_move)
        if result == 'draw':
            print("IT'S A DRAW!")
        elif result:
            print("YOUR DEFENCE IS SUCCESSFUL!")
        else:
            self.decrease_health()
            print("YOUR DEFENCE IS FAILED!")

    def __repr__(self) -> str:
        """
        Implement a human readable string representation for Player class
        """

        return f"Name = {self.name}, score = {self.score}, health = {self.health}"

    def __str__(self) -> str:
        """
        Implement type-casting for Player.
        Player cast to string type equals to its name and score
        """

        return f"{self.name}, {self.score}"
