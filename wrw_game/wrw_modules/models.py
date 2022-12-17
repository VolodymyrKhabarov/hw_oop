"""
This module implements Enemy and Player classes.
The enemy model represents the playing enemy-bot.
All choices made by this model are random.
Player model is controlled by the user.
It represents a playing user.
All choices are controlled by the user.
"""
import sys
from random import randint

from wrw_modules import exceptions
from wrw_modules import settings


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
            raise exceptions.EnemyDown(self.level)
        return self.health

    def select_attack(self):
        """
        Return a random attack choice from valid choices.
        """

        bot_choice = self.select_fight_choice()
        return bot_choice

    def select_defense(self):
        """
        Return a random defense choice from valid choices.
        """

        bot_choice = self.select_fight_choice()
        return bot_choice

    @staticmethod
    def select_fight_choice():
        """Returns a random choice for an enemy attack or defense"""

        bot_fighter = settings.VALID_CHOICES[randint(0, 2)]
        return bot_fighter

    def __repr__(self) -> str:
        """
        Implement a human readable string representation for Enemy class
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
            raise exceptions.GameOver(self)
        return self.health

    def select_attack(self):
        """
        Return an attack choice made by the user.
        """

        player_choice = self.select_fight_choice()
        return player_choice

    def select_defense(self):
        """
        Return a defense choice made by the user.
        """

        player_choice = self.select_fight_choice()
        return player_choice

    @staticmethod
    def select_fight_choice():
        """Returns a choice for an player attack or defense. Performs choice validation"""

        while True:
            print('MAKE A FIGHT CHOICE FROM (WARRIOR - 1, ROBBER - 2, WIZARD - 3): ')
            player_choice = input()
            if player_choice in settings.VALID_CHOICES:
                return settings.VALID_CHOICES[int(player_choice) - 1]

    @staticmethod
    def fight(player_choice, bot_choice):
        """
        Static method to perform a fight.
        Takes two arguments representing attack and defense choices.
        Performs fight result calculation and return it back.
        """

        if player_choice == bot_choice:
            return settings.DRAW
        battle = (player_choice, bot_choice)
        if battle in settings.WIN_CONDITION:
            return settings.WIN
        return settings.LOSE

    def attack(self, enemy):
        """
        Perform attack on an enemy instance.
        """

        try:
            player_choice = self.select_attack()
            bot_choice = enemy.select_defense()
            result = self.fight(player_choice, bot_choice)
            if result == settings.DRAW:
                print("IT'S A DRAW!")
            elif result == settings.WIN:
                enemy.decrease_health()
                self.score += 1
                print("YOUR ATTACK IS SUCCESSFUL!")
            else:
                print("YOUR ATTACK IS FAILED!")
        except exceptions.EnemyDown:
            self.score += settings.REWARD
            raise

    def defense(self, enemy):
        """
        Perform defense from an enemy attack.
        """

        try:
            player_choice = self.select_defense()
            bot_choice = enemy.select_attack()
            result = self.fight(player_choice, bot_choice)
            if result == settings.DRAW:
                print("IT'S A DRAW!")
            elif result == settings.WIN:
                print("YOUR DEFENSE IS SUCCESSFUL!")
            else:
                self.decrease_health()
                print("YOUR DEFENSE IS FAILED!")
        except exceptions.GameOver as msg:
            with open('scores.txt', 'a', encoding='utf-8') as file:
                file.write(f'Name: {self.name}, score: {self.score}\n')
            print(msg)
            sys.exit()

    def __repr__(self) -> str:
        """
        Implement a human readable string representation for Player class
        """

        return f"Name = {self.name}, score = {self.score}, health = {self.health}"
