"""
    Project name: JustGet10
    Copyright,

    ALEV Samuel (226430@supinfo.com)
    STOCKMAN Jim (227078@supinfo.com)
    (C) 2016 - 2017

    This script was tested with Python 3.5.2 and PyGame 1.9.2b1
"""

import random


# Erzeugt die Elemente mit Wahrscheinlichkeit
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


# Gibt das Spielfeld mit Zufallselementen zurück
def newBoard(n: int, tuple: tuple):
    board = []

    for i in range(n):  # Fügt dem Spielfeld die Zahlen hinzu
        board.append([element(tuple) for i in range(n)])
    return board


# Spielfeld anzeigen
def display(board: list, n: int):
    for n in board:
        for number in n:
            print(number, end=' ')
        print('\n')