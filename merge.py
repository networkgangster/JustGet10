"""
    Project name: JustGet10
    Copyright,

    ALEV Samuel (226430@supinfo.com)
    STOCKMAN Jim (227078@supinfo.com)
    (C) 2016 - 2017

    This script was tested with Python 3.5.2 and PyGame 1.9.2b1
"""

import bases


def propagation(n: int, board: list, coord: tuple, liste: list):
    if 0 <= coord[0] < n and 0 <= coord[1] < n:
        if coord[0] - 1 >= 0:
            if board[coord[0] - 1][coord[1]] == board[coord[0]][coord[1]]:
                if (coord[0] - 1, coord[1]) not in liste:
                    liste.append((coord[0] - 1, coord[1]))
                    propagation(n, board, (coord[0] - 1, coord[1]), liste)
        if coord[0] + 1 < n:
            if board[coord[0] + 1][coord[1]] == board[coord[0]][coord[1]]:
                if (coord[0] + 1, coord[1]) not in liste:
                    liste.append((coord[0] + 1, coord[1]))
                    propagation(n, board, (coord[0] + 1, coord[1]), liste)
        if coord[1] - 1 >= 0:
            if board[coord[0]][coord[1] - 1] == board[coord[0]][coord[1]]:
                if (coord[0], coord[1] - 1) not in liste:
                    liste.append((coord[0], coord[1] - 1))
                    propagation(n, board, (coord[0], coord[1] - 1), liste)
        if coord[1] + 1 < n:
            if board[coord[0]][coord[1] + 1] == board[coord[0]][coord[1]]:
                if (coord[0], coord[1] + 1) not in liste:
                    liste.append((coord[0], coord[1] + 1))
                    propagation(n, board, (coord[0], coord[1] + 1), liste)


def modification(n: int, board: list, liste: list):
    board[liste[0][0]][liste[0][1]] += 1
    for i in range(1, len(liste)):
        board[liste[i][0]][liste[i][1]] = 0


def gravity(n: int, board: list, proba: tuple):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and i >= 1:
                if i == 1:
                    board[i][j] = board[i - 1][j]
                    board[0][j] = 0
                elif i == 2:
                    board[2][j] = board[i - 1][j]
                    board[1][j] = board[i - 2][j]
                    board[0][j] = 0
                elif i == 3:
                    board[i][j] = board[i - 1][j]
                    board[2][j] = board[i - 2][j]
                    board[1][j] = board[i - 3][j]
                    board[0][j] = 0
                elif i == 4:
                    board[i][j] = board[i - 1][j]
                    board[3][j] = board[i - 2][j]
                    board[2][j] = board[i - 3][j]
                    board[1][j] = board[i - 4][j]
                    board[0][j] = 0
                elif i == 5:
                    board[i][j] = board[i - 1][j]
                    board[4][j] = board[i - 2][j]
                    board[3][j] = board[i - 3][j]
                    board[2][j] = board[i - 4][j]
                    board[1][j] = board[i - 5][j]
                    board[0][j] = 0
    for p in range(n):
        for m in range(n):
            if board[p][m] == 0:
                board[p][m] = bases.element(proba)
