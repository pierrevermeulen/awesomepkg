# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for awesomepkg Project
"""

import random
from os.path import split
from time import sleep

def try_me():
    print("This package is awesome !!!")
    print("And completely useless...")
    print("But you can play rock/paper/scissors:")
    move_list = ['R', 'P', 'S']
    while True:
        move = input("Choose a move: R/P/S/E(xit): ").upper()
        sleep(1)
        if move in move_list:
            print('Your move: '+move)
            c_move = random.choice(move_list)
            print('Computer move: '+c_move)
            if move == c_move:
                print('    -> Tie')
            elif (move == 'R' and c_move == 'S') or \
                (move == 'S' and c_move == 'P') or \
                (move == 'P' and c_move == 'R'):
                print('    -> You win!')
            else:
                print('    -> You lose!')
        elif move in ['E', 'Exit']:
            break
        else:
            print('Invalid move, try again')


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    try_me()
