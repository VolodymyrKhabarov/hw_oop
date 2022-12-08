"""
This module has a description and rules of WRW game
"""
import sys

from . import engine
from . import rules


def menu():
    """
    This function represents game menu
    """
    choice = None
    while choice != "0":
        print(
            """
            GAME MENU

            0 - QUIT
            1 - RULES
            2 - PLAY
            """
            )

        choice = input("Choice: ")
        print()

        if choice == "0":
            print('GOOD BYE!')
            sys.exit()
        elif choice == "1":
            rules.get_rules()
        elif choice == "2":
            engine.play()
