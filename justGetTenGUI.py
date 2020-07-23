'''
    Project name: JustGet10
    Copyright,

    ALEV Samuel (226430@supinfo.com)
    STOCKMAN Jim (227078@supinfo.com)
    (C) 2016 - 2017

    This script was tested with Python 3.5.2 and PyGame 1.9.2b1
'''

import pygame, bases, possibles, merge

pygame.init()
pygame.font.init()

# Var font
roboto = pygame.font.Font("fonts/Roboto.ttf", 30)

# Var couleur
black = (0, 0, 0)

# Var Höhe und Breite des Fensters
display_width = 800
display_height = 600

# Dictionary für Bilder
dic = {
    'logo': {
        'img': pygame.image.load('images/logo.png'),
        'x': (display_width * 0.5) - 251 / 2,
        'y': (display_height * 0.2) - 103 / 2
    },
    'play': {
        'img': pygame.image.load('images/boutons/jouer.png'),
        'img_pressed': pygame.image.load('images/boutons/jouer_pressed.png'),
        'x': (display_width * 0.5) - 290 / 2,
        'y': (display_height * 0.55) - 72 / 2
    },
    'quitter': {
        'img': pygame.image.load('images/boutons/quitter.png'),
        'img_pressed': pygame.image.load('images/boutons/quitter_pressed.png'),
        'x': (display_width * 0.5) - 290 / 2,
        'y': (display_height * 0.7) - 72 / 2
    },
    'petite': {
        'img': pygame.image.load('images/boutons/petite.png'),
        'img_pressed': pygame.image.load('images/boutons/petite_pressed.png'),
        'x': (display_width * 0.5) - 290 / 2,
        'y': (display_height * 0.55) - 72 / 2
    },
    'moyenne': {
        'img': pygame.image.load('images/boutons/moyenne.png'),
        'img_pressed': pygame.image.load('images/boutons/moyenne_pressed.png'),
        'x': (display_width * 0.5) - 290 / 2,
        'y': (display_height * 0.7) - 72 / 2
    },
    'grande': {
        'img': pygame.image.load('images/boutons/grande.png'),
        'img_pressed': pygame.image.load('images/boutons/grande_pressed.png'),
        'x': (display_width * 0.5) - 290 / 2,
        'y': (display_height * 0.85) - 72 / 2,
    },
    'retour': {
        'img': pygame.image.load('images/boutons/retour.png'),
        'img_pressed': pygame.image.load('images/boutons/retour_pressed.png'),
        'x': (display_width * 0.5) - 128 / 2,
        'y': (display_height * 0.43) - 45 / 2,
    },
    'limPerCase': {
        'enable': pygame.image.load('images/boutons/enable.png'),
        'disable': pygame.image.load('images/boutons/disable.png'),
        'x': (display_width * 0.7) - 290 / 2 + 140,
        'y': (display_height * 0.55) - 72 / 2
    },
    'limPerGame': {
        'enable': pygame.image.load('images/boutons/enable.png'),
        'disable': pygame.image.load('images/boutons/disable.png'),
        'x': (display_width * 0.7) - 290 / 2 + 140,
        'y': (display_height * 0.7) - 72 / 2
    },
    'start': {
        'img': pygame.image.load('images/boutons/commencer.png'),
        'img_pressed': pygame.image.load('images/boutons/commencer_pressed.png'),
        'x': (display_width * 0.5) - 290 / 2,
        'y': (display_height * 0.85) - 72 / 2
    },
    'restart': {
        'img': pygame.image.load('images/boutons/restart.png'),
        'img_pressed': pygame.image.load('images/boutons/restart_pressed.png'),
        'x': (display_width * 0.85) - 145 / 2,
        'y': (display_height * 0.5) - 37 / 2
    },
    'quitter2': {
        'img': pygame.image.load('images/boutons/quitterPetit.png'),
        'img_pressed': pygame.image.load('images/boutons/quitterPetit_pressed.png'),
        'x': (display_width * 0.85) - 145 / 2,
        'y': (display_height * 0.6) - 37 / 2
    },
    'back': {
        'img': pygame.image.load('images/back.png'),
        'x': 590,
        'y': 32
    },
    'back2': {
        'img': pygame.image.load('images/back.png'),
        'x': 590,
        'y': 72
    },
    'lose': {
        'sound': pygame.mixer.Sound("sounds/lose.ogg")
    },
    'doritos': {
        'img': pygame.image.load('images/dorito.png'),
        'x': 1,
        'y': 1,
    },
    'airhorn': {
        'sound': pygame.mixer.Sound("sounds/airhorn.ogg")
    },
}

# Var für Spielstart
n = 5
proba = (0.05, 0.30, 0.6)
board = []
limCase = False
limGame = False
saved = False



# Bestimmt die Größe des Fensters, setzt einen Titel und ein Symbol
gameDisplay = pygame.display.set_mode((display_width, display_height), 0, 32)
pygame.display.set_caption("Just Get 10")
pygame.display.set_icon(dic['logo']['img'])

# Var Spieluhr
clock = pygame.time.Clock()
FPS = 60

# Var texte
texte1 = roboto.render('Temps limité par coup', True, (0, 0, 0))
texte2 = roboto.render('Temps limité pour terminer', True, (0, 0, 0))

mlg2 = True


def blit(angle):
    for i in range(10):
        gameDisplay.blit(pygame.transform.rotate(dic['doritos']['img'], angle), (dic['doritos']['x'] * i * 100, dic['doritos']['y']))

# noinspection PyTypeChecker
def menu():
    # Hintergrund
    gameDisplay.fill((255, 251, 234))

    # Anzeige der Buttons im Hauptmenü
    gameDisplay.blit(dic['logo']['img'], (dic['logo']['x'], dic['logo']['y']))
    gameDisplay.blit(dic['play']['img'], (dic['play']['x'], dic['play']['y']))
    gameDisplay.blit(dic['quitter']['img'], (dic['quitter']['x'], dic['quitter']['y']))

    inMenu1 = True
    while inMenu1:
        # Ruft die x-, y-Position des Cursors bei jedem Schleifendurchlauf ab
        mouse = pygame.mouse.get_pos()

        # Erlaubt events zu verwalten
        for event in pygame.event.get():
            # Fügt dem Schließen-Button eine Aktion hinzu
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            # Test click auf "Play" Button
            if dic['play']['x'] + 290 > mouse[0] > dic['play']['x'] and dic['play']['y'] + 72 > mouse[1] > dic['play']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['play']['img'], (dic['play']['x'], dic['play']['y']))
                    inMenu1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['play']['img_pressed'], (dic['play']['x'], dic['play']['y']))
            else:
                gameDisplay.blit(dic['play']['img'], (dic['play']['x'], dic['play']['y']))

            # Test click auf "Quit" Button
            if dic['quitter']['x'] + 290 > mouse[0] > dic['quitter']['x'] and dic['quitter']['y'] + 72 > mouse[1] > dic['quitter']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['quitter']['img'], (dic['quitter']['x'], dic['quitter']['y']))
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['quitter']['img_pressed'], (dic['quitter']['x'], dic['quitter']['y']))
            else:
                gameDisplay.blit(dic['quitter']['img'], (dic['quitter']['x'], dic['quitter']['y']))

        pygame.display.update()
        clock.tick(FPS)

    # Wechselt zum Menü mit der Schwierigkeit, wenn die Schleife beendet ist
    menu2()


# noinspection PyTypeChecker
def menu2():
    # Hintergrund
    gameDisplay.fill((255, 251, 234))

    # Anzeige der Buttons im Hauptmenü
    gameDisplay.blit(dic['logo']['img'], (dic['logo']['x'], dic['logo']['y']))
    gameDisplay.blit(dic['petite']['img'], (dic['petite']['x'], dic['petite']['y']))
    gameDisplay.blit(dic['moyenne']['img'], (dic['moyenne']['x'], dic['moyenne']['y']))
    gameDisplay.blit(dic['grande']['img'], (dic['grande']['x'], dic['grande']['y']))
    gameDisplay.blit(dic['retour']['img'], (dic['retour']['x'], dic['retour']['y']))

    inMenu2 = True
    while inMenu2:
        global n
        # Ruft die x-, y-Position des Cursors bei jedem Schleifendurchlauf ab
        mouse = pygame.mouse.get_pos()

        # Erlaubt events zu verwalten
        for event in pygame.event.get():
            # Fügt dem Schließen-Button eine Aktion hinzu
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            # Test click auf "Zurück" Button
            if dic['retour']['x'] + 128 > mouse[0] > dic['retour']['x'] and dic['retour']['y'] + 45 > mouse[1] > dic['retour']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['retour']['img'], (dic['retour']['x'], dic['retour']['y']))
                    # Zurück zum Hauptmenü
                    inMenu2 = False
                    menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['retour']['img_pressed'], (dic['retour']['x'], dic['retour']['y']))
            else:
                gameDisplay.blit(dic['retour']['img'], (dic['retour']['x'], dic['retour']['y']))

            # Test click auf "Petite" Button
            if dic['petite']['x'] + 290 > mouse[0] > dic['petite']['x'] and dic['petite']['y'] + 72 > mouse[1] > dic['petite']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['petite']['img'], (dic['petite']['x'], dic['petite']['y']))
                    n = 6
                    inMenu2 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['petite']['img_pressed'], (dic['petite']['x'], dic['petite']['y']))
            else:
                gameDisplay.blit(dic['petite']['img'], (dic['petite']['x'], dic['petite']['y']))

            # Test click auf "Moyenne" Button
            if dic['moyenne']['x'] + 290 > mouse[0] > dic['moyenne']['x'] and dic['moyenne']['y'] + 72 > mouse[1] > dic['moyenne']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['moyenne']['img'], (dic['moyenne']['x'], dic['moyenne']['y']))
                    n = 5
                    inMenu2 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['moyenne']['img_pressed'], (dic['moyenne']['x'], dic['moyenne']['y']))
            else:
                gameDisplay.blit(dic['moyenne']['img'], (dic['moyenne']['x'], dic['moyenne']['y']))

            # Test click auf "Grande" Button
            if dic['grande']['x'] + 290 > mouse[0] > dic['grande']['x'] and dic['grande']['y'] + 72 > mouse[1] > dic['grande']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['grande']['img'], (dic['grande']['x'], dic['grande']['y']))
                    n = 4
                    inMenu2 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['grande']['img_pressed'], (dic['grande']['x'], dic['grande']['y']))
            else:
                gameDisplay.blit(dic['grande']['img'], (dic['grande']['x'], dic['grande']['y']))

        pygame.display.update()
        clock.tick(FPS)

    # Wechselt zum Menü mit den Optionen, wenn die Schleife beendet ist
    menu3()


# noinspection PyTypeChecker
def menu3():
    gameDisplay.fill((255, 251, 234))

    # Zeigt die Buttons des Hauptmenüs an
    gameDisplay.blit(dic['logo']['img'], (dic['logo']['x'], dic['logo']['y']))
    gameDisplay.blit(dic['limPerCase']['disable'], (dic['limPerCase']['x'], dic['limPerCase']['y']))
    gameDisplay.blit(dic['limPerGame']['disable'], (dic['limPerGame']['x'], dic['limPerGame']['y']))
    gameDisplay.blit(texte1, (dic['limPerCase']['x'] - 375, dic['limPerCase']['y'] + 10))
    gameDisplay.blit(texte2, (dic['limPerGame']['x'] - 375, dic['limPerGame']['y'] + 10))
    gameDisplay.blit(dic['retour']['img'], (dic['retour']['x'], dic['retour']['y']))
    gameDisplay.blit(dic['start']['img'], (dic['start']['x'], dic['start']['y']))

    global limCase
    global limGame

    inMenu3 = True
    while inMenu3:
        # Ruft die x-, y-Position des Cursors bei jedem Schleifendurchlauf ab
        mouse = pygame.mouse.get_pos()

        # Erlaubt events zu verwalten
        for event in pygame.event.get():
            # Fügt dem Schließen-Button eine Aktion hinzu
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            # Test click auf "Zurück" Button
            if dic['retour']['x'] + 128 > mouse[0] > dic['retour']['x'] and dic['retour']['y'] + 45 > mouse[1] > dic['retour']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['retour']['img'], (dic['retour']['x'], dic['retour']['y']))
                    # Zurück zum Hauptmenü
                    inMenu3 = False
                    menu2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['retour']['img_pressed'], (dic['retour']['x'], dic['retour']['y']))
            else:
                gameDisplay.blit(dic['retour']['img'], (dic['retour']['x'], dic['retour']['y']))

            # Test click auf "Start" Button
            if dic['start']['x'] + 290 > mouse[0] > dic['start']['x'] and dic['start']['y'] + 72 > mouse[1] > dic['start']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['start']['img'], (dic['start']['x'], dic['start']['y']))
                    # Stoppt die Schleife um das Spiel zu beginnen
                    inMenu3 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['start']['img_pressed'], (dic['start']['x'], dic['start']['y']))
            else:
                gameDisplay.blit(dic['start']['img'], (dic['start']['x'], dic['start']['y']))

            # Test click auf "limPerCase" Button
            if dic['limPerCase']['x'] + 290 > mouse[0] > dic['limPerCase']['x'] and dic['limPerCase']['y'] + 72 > mouse[1] > dic['limPerCase']['y']:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if limCase:
                        limCase = False
                    else:
                        limCase = True
                    if limCase:
                        gameDisplay.blit(dic['limPerCase']['enable'], (dic['limPerCase']['x'], dic['limPerCase']['y']))
                    else:
                        gameDisplay.blit(dic['limPerCase']['disable'], (dic['limPerCase']['x'], dic['limPerCase']['y']))

            # Test click auf "limPerGame" Button
            if dic['limPerGame']['x'] + 290 > mouse[0] > dic['limPerGame']['x'] and dic['limPerGame']['y'] + 72 > mouse[1] > dic['limPerGame']['y']:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if limGame:
                        limGame = False
                    else:
                        limGame = True
                    if limGame:
                        gameDisplay.blit(dic['limPerGame']['enable'], (dic['limPerGame']['x'], dic['limPerGame']['y']))
                    else:
                        gameDisplay.blit(dic['limPerGame']['disable'], (dic['limPerGame']['x'], dic['limPerGame']['y']))
        pygame.display.update()
        clock.tick(FPS)

    # Spielen...
    game(n, board)

palette = [
    (127, 0, 255),  #0 Purple
    (0, 255, 255),  #1 Cyan
    (0, 128, 255),  #2 Sky
    (0, 0, 255),    #3 Blue
    (178, 255, 102),#4 Lime
    (0, 255, 0),    #5 Green
    (255, 255, 0),  #6 Yellow
    (255, 128, 0),  #7 Orange
    (255, 0, 0),    #8 Red
    (255, 0, 255),  #9 Pink
]


def cellColor(board: list, surface: pygame.Surface, coord: tuple, selected: bool):
    x, y = 60,60
    number = board[coord[0]][coord[1]]%10
    if selected:
        color = (255, 255, 255)
    else:
        color = palette[number]
    pygame.draw.rect(surface, color, ((coord[1]*(128-32*(n-4)))+x, (coord[0]*(128-32*(n-4)))+y, (128-32*(n-4)),(128-32*(n-4))), 0)


def cellValue(board: list, surface: pygame.Surface, coord: tuple, selected: bool):
    x, y = 60 + (64-16*(n-4)), 60 + (64-16*(n-4))

    textSurface = roboto.render(str(board[coord[0]][coord[1]]), True, (0, 0, 0))
    textRect = textSurface.get_rect()
    textRect.center = ((coord[1]*(128-32*(n-4)))+x, (coord[0]*(128-32*(n-4)))+y)
    surface.blit(textSurface, textRect)


def displayBoard(board: list, n: int, surface: pygame.Surface):
    for p in range(len(board)):
        for m in range(len(board[0])):
            cellColor(board, surface, (p, m), False)
            cellValue(board, surface, (p, m), False)

occurence = 0


def maxScore(n, board: list):
    global occurence
    gameDisplay.fill((255, 251, 234))
    maxNumber = possibles.maxNumber(n, board)
    scoreSurface = roboto.render(str(maxNumber), True, (0, 0, 0))
    gameDisplay.blit(scoreSurface, (680, 200))

    textSurface = roboto.render('Current Score', True, (0, 0, 0))
    gameDisplay.blit(textSurface, (600, 150))

    while maxNumber == 10 and occurence == 0:
        dic['airhorn']['sound'].set_volume(0.2)
        dic['airhorn']['sound'].play()

        angle = 0
        while mlg2:
            gameDisplay.fill((255, 251, 234))
            # Update button
            displayBoard(board, n, gameDisplay)
            gameDisplay.blit(textSurface, (600, 150))
            gameDisplay.blit(scoreSurface, (680, 200))
            angle += 10
            blit(angle)
            if dic['doritos']['y'] > 500 and occurence < 1:
                angle = 0
                dic['doritos']['y'] = 1
                occurence += 1
                blit(angle)
            if occurence >= 1 and dic['doritos']['y'] > 600:
                break
            dic['doritos']['y'] += 20
            pygame.display.update()
            clock.tick(20)
        break


def game(n, board):
    gameDisplay.fill((255, 251, 234))
    global saved
    if not saved:
        board = bases.newBoard(n, proba)
    doubleclick = 0
    click = []
    maxScore(n, board)
    displayBoard(board, n, gameDisplay)

    InGame2 = possibles.playableCase(n, board)

    counterGame, textGame = 300, str(300)
    counterCase, textCase = 10, str(10)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    inGame = True
    while inGame:
        while InGame2:
            InGame2 = possibles.playableCase(n, board)
            mouse = pygame.mouse.get_pos()

            # Erlaubt Events zu verwalten
            for event in pygame.event.get():
                # Fügt dem Schließen-Button eine Aktion hinzu
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                # Timer für Spielende
                if limGame:
                    if event.type == pygame.USEREVENT:
                        counterGame -= 1
                        if counterGame >= 0:
                            textGame = str(counterGame)
                        else:
                            gameDisplay.blit(dic['back']['img'], (dic['back']['x'], dic['back']['y']))

                            InGame2 = False
                    else:
                        gameDisplay.blit(dic['back']['img'], (dic['back']['x'], dic['back']['y']))
                        gameDisplay.blit(roboto.render(textGame + ' sec', True, (0, 0, 0)), (600, 32))

                # Zeitlimit-Stoppuhr pro Box
                if limCase:
                    if event.type == pygame.USEREVENT:
                        counterCase -= 1
                        if counterCase >= 0:
                            textCase = str(counterCase)
                        else:
                            gameDisplay.blit(dic['back2']['img'], (dic['back2']['x'], dic['back2']['y']))
                            InGame2 = False
                    else:
                        gameDisplay.blit(dic['back2']['img'], (dic['back2']['x'], dic['back2']['y']))
                        gameDisplay.blit(roboto.render(textCase + ' sec', True, (0, 0, 0)), (600, 72))

                # Test click auf Kästchen
                for colonne in range(len(board)):
                    for ligne in range(len(board)):
                        if (ligne*(128-32*(n-4)))+60 + (128-32*(n-4)) > mouse[1] > (ligne*(128-32*(n-4)))+60 and (colonne*(128-32*(n-4)))+60 + (128-32*(n-4)) > mouse[0] > (colonne*(128-32*(n-4)))+60:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click.append((ligne, colonne))
                                if possibles.possessAdjacent(n, board, ligne, colonne):
                                    current = (ligne, colonne)
                                    listeAdja = [current]
                                    merge.propagation(n, board, current, listeAdja)
                                    for elem in range(len(listeAdja)):
                                        cellColor(board, gameDisplay, (listeAdja[elem][0], listeAdja[elem][1]), True)
                                        cellValue(board, gameDisplay, (listeAdja[elem][0], listeAdja[elem][1]), True)
                                    doubleclick += 1
                                    try:
                                        if click[0][0] == click[1][0] and click[0][1] == click[1][1] and doubleclick == 2:
                                            merge.modification(n, board, listeAdja)
                                            merge.gravity(n, board, proba)
                                            counterCase, textCase = 10, str(10)
                                            maxScore(n, board)
                                        else:
                                            for elem in range(len(listeAdja)):
                                                cellColor(board, gameDisplay, (listeAdja[elem][0], listeAdja[elem][1]), False)
                                                cellValue(board, gameDisplay, (listeAdja[elem][0], listeAdja[elem][1]), False)
                                        doubleclick = 0
                                        click = []
                                        displayBoard(board, n, gameDisplay)
                                        if limGame:
                                            gameDisplay.blit(roboto.render(textGame + ' sec', True, (0, 0, 0)), (600, 32))
                                        if limCase:
                                            gameDisplay.blit(roboto.render(textCase + ' sec', True, (0, 0, 0)), (600, 72))
                                    except IndexError: pass
            pygame.display.update()
            clock.tick(FPS)

        # Verloren? Neu anfangen oder aufhören?
        gameDisplay.blit(dic['restart']['img'], (dic['restart']['x'], dic['restart']['y']))
        gameDisplay.blit(dic['quitter2']['img'], (dic['quitter2']['x'], dic['quitter2']['y']))
        dic['lose']['sound'].set_volume(0.2)
        dic['lose']['sound'].play()

        mouse = pygame.mouse.get_pos()
        # Erlaubt events zu verwalten
        for event in pygame.event.get():
            # Fügt dem Schließen-Button eine Aktion hinzu
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Test click auf "Restart" Button
            if dic['restart']['x'] + 148 > mouse[0] > dic['restart']['x'] and dic['restart']['y'] + 37 > mouse[1] > dic['restart']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['restart']['img'], (dic['restart']['x'], dic['restart']['y']))
                    dic['lose']['sound'].stop()
                    game(n, bases.newBoard(n, proba))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['restart']['img_pressed'], (dic['restart']['x'], dic['restart']['y']))
            else:
                gameDisplay.blit(dic['restart']['img'], (dic['restart']['x'], dic['restart']['y']))

            # Test click auf "Quitter" Button
            if dic['quitter2']['x'] + 148 > mouse[0] > dic['quitter2']['x'] and dic['quitter2']['y'] + 37 > mouse[1] > dic['quitter2']['y']:
                if event.type == pygame.MOUSEBUTTONUP:
                    gameDisplay.blit(dic['quitter2']['img'], (dic['quitter2']['x'], dic['quitter2']['y']))
                    dic['lose']['sound'].stop()
                    saved = False
                    menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameDisplay.blit(dic['quitter2']['img_pressed'], (dic['quitter2']['x'], dic['quitter2']['y']))
            else:
                gameDisplay.blit(dic['quitter2']['img'], (dic['quitter2']['x'], dic['quitter2']['y']))
        pygame.display.update()
        clock.tick(FPS)

# Starten der Funktion, die das Menü anzeigt
menu()

# Prozess abschließen
pygame.quit()
quit()
