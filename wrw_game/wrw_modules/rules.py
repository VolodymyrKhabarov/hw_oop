"""
This module has a description and rules of WRW game
"""

def get_rules():
    """
    This function has a description and rules of WRW game
    """

    print("""
    RULES:
    
    Warriors, robbers and wizards (WRW) game is a "Paper, Rock and Scissors" clone,
    but in a fantasy setting. The player's goal is to gain as many score points, as it possible.
    
    The game process is divided into rounds. Each round consists of **attack** and
    **defence** stages. Rounds are repeated, until player is defeated.
    
    It's simple...
    
    - **Warrior** beats **Robber**
    - **Robber** beats **Wizard**
    - **Wizard** beats **Warrior**
    
    At the beginning of WRW game player has 5 health points, and the enemy has 1 level and 1 health point.
    
    Attack Stage
    ============
    
    Player selects the choice to attack from **warrior**, **robber** or **wizard**,
    enemy selects the choice for defence from the same options by random. If the
    attack is successful:
    
    - enemy health is decreased by one point
    - player gains one point
    
    In case enemy is defeated:
    
    - a new enemy instance is initialized using higher level
    - player gains 5 points
    - next defence stage is skipped, and player attacks again
    
    Defence Stage
    =============
    
    Player selects the choice to defend from **warrior**, **robber** or **wizard**,
    enemy selects the choice to attack from the same options by random. If the
    attack is successful:
    
    - player health is decreased by one point
    """)
