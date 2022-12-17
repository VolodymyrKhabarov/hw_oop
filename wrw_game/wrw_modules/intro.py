"""
This module has a description and rules of WRW game
"""
import sys

from wrw_modules import engine


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
            sys.exit()
        elif choice == "1":
            with open('rules.txt', encoding='utf-8') as file:
                for line in file:
                    print(line)
        elif choice == "2":
            engine.play()
