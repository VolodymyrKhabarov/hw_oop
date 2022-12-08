"""
This module is for start the WRW game menu
"""
import sys

from wrw_modules import intro

if __name__ == '__main__':
    try:
        intro.menu()
    except KeyboardInterrupt:
        print('GOOD BYE!')
        sys.exit()
