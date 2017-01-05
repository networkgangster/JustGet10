"""
    Project name: JustGet10
    Copyright,

    ALEV Samuel (226430@supinfo.com)
    STOCKMAN Jim (227078@supinfo.com)
    (C) 2016 - 2017

    This script was tested with Python 3.5.2 and PyGame 1.9.2b1
"""

import random


# Génère les élements avec probabilité
def element(tuple: tuple):
    nb = random.random()

    if nb < tuple[0]:
        return 4
    elif tuple[0] < nb < tuple[1]:
        return 3
    elif tuple[1] < nb < tuple[2]:
        return 2
    else:
        return 1


# Retourne une board avec les éléments aléatoires
def newBoard(n: int, tuple: tuple):
    board = []

    for i in range(n):  # Ajoute les chiffres au board
        board.append([element(tuple) for i in range(n)])
    return board


# Affiche la board
def display(board: list, n: int):
    for n in board:
        for number in n:
            print(number, end=' ')
        print('\n')