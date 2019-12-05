"""
Game where two players take in and out sticks.
Specifically,
1. The game begins with a number of sticks on a table (between 10 and 100)
2. Each player, in turn, takes between 1-3 sticks off the table.
3. The player to take the last stick loses.
"""

import random
import sys


player_01 = str(input("Enter your name, player 01: "))
player_02 = str(input("Enter your name, player 02: "))


found_num_sticks = False
while not found_num_sticks:
    try:
        num_sticks = int(input("So, how many sticks would you like to play with?: "))
        if num_sticks < 10 or num_sticks > 100:
            raise Exception("Sorry too many or too few sticks! Try again.")
        else:
            found_num_sticks = True
    except Exception as e:
        print(e)
        continue

who_goes = random.randint(0,1)
playing_game = True
while playing_game:
    if who_goes == 1:
        p1_goes = True
        while p1_goes:
            try:
                p1_sticks = int(input(f"So, {player_01}, how many sticks ya want?: "))
                if p1_sticks < 1 or p1_sticks > 3:
                    raise Exception("Sorry that's too many or too few sticks! Try again.")
                else:
                    num_sticks -= p1_sticks
                    if num_sticks == 0 or num_sticks < 0:
                        print(f"Ha, {player_01}, you lost!")
                        sys.exit()
                    print(f"There are {num_sticks} in your table")
                    who_goes = 0
                    p1_goes = False
            except Exception as e:
                print(e)
                continue
    if who_goes == 0:
        p2_goes = True
        while p2_goes:
            try:
                p2_sticks = int(input(f"So, {player_02}, how many sticks ya want?: "))
                if p2_sticks < 1 or p2_sticks > 3:
                    raise Exception("Sorry that's too many or too few sticks! Try again.")
                else:
                    num_sticks -= p2_sticks
                    if num_sticks == 0 or num_sticks < 0:
                        print(f"Ha, {player_02}, you lost!")
                        sys.exit()
                    print(f"There are {num_sticks} in your table")
                    who_goes = 1
                    p2_goes = False
            except Exception as e:
                print(e)
                continue
