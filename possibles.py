"""
    Project name: JustGet10
    Copyright,

    ALEV Samuel (226430@supinfo.com)
    STOCKMAN Jim (227078@supinfo.com)
    (C) 2016 - 2017

    This script was tested with Python 3.5.2 and PyGame 1.9.2b1
"""


# Vérifie si une case avec les coordonnées i et j ont une case adjacente
def possessAdjacent(n: int, board: list, i: int, j: int):
    # Debug au cas où i ou j est 'out of range'
    if not 0 <= i < n or not 0 <= j < n: return 'Error'
    if i + 1 < n:
        if board[i + 1][j] == board[i][j]: return True
    if j + 1 < n:
        if board[i][j + 1] == board[i][j]: return True
    if 0 <= j - 1:
        if board[i][j - 1] == board[i][j]: return True
    if 0 <= i - 1:
        if board[i - 1][j] == board[i][j]: return True
    return False


# Vérifie si la board possède encore des cases adjacentes
def playableCase(n: int, board: list):
    for i in range(n):
        for j in range(n):
            if possessAdjacent(n, board, i, j):
                return True
    return False


# Recherche le nombre le plus grand dans une liste
def maxNumber(n: int, board: list):
    nbMax = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] > nbMax:
                nbMax = board[i][j]
    return nbMax