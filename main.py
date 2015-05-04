import pygame
import time
import random
import math


def init():
    global screenSize, background, gridColor, cellColor, cellSize, A, pre
    global screen, hCells, vCells, ind, displayGrid, secondsInbetween
    screenSize = (400, 600)
    background = (255, 255, 255)
    gridColor = (125, 125, 125)
    cellColor = (255, 0, 0)
    cellSize = 40
    secondsInbetween = 0.2
    displayGrid = False
    ind = [(-1, -1),
           (-1, 0),
           (-1, 1),
           (0, -1),
           (0, 1),
           (1, -1),
           (1, 0),
           (1, 1)]

    try:
        with open('settings.cfg', 'r') as f:
            for line in f:
                val = float(line.split()[-1])
                if 'height = ' in line:
                    screenSize = (screenSize[0], int(val))
                if 'width = ' in line:
                    screenSize = (int(val), screenSize[1])
                if 'bgRed = ' in line:
                    background = (int(val), background[1], background[2])
                if 'bgGreen = ' in line:
                    background = (background[0], int(val), background[2])
                if 'bgBlue = ' in line:
                    background = (background[0], background[1], int(val))
                if 'gridRed = ' in line:
                    gridColor = (int(val), gridColor[1], gridColor[2])
                if 'gridGreen = ' in line:
                    gridColor = (gridColor[0], int(val), gridColor[2])
                if 'gridBlue = ' in line:
                    gridColor = (gridColor[0], gridColor[1], int(val))
                if 'cellRed = ' in line:
                    cellColor = (int(val), cellColor[1], cellColor[2])
                if 'cellGreen = ' in line:
                    cellColor = (cellColor[0], int(val), cellColor[2])
                if 'cellBlue = ' in line:
                    cellColor = (cellColor[0], cellColor[1], int(val))
                if 'cellSize = ' in line:
                    cellSize = int(val)
                if 'secondsInbetween' in line:
                    secondsInbetween = val
                if 'displayGrid = ' in line:
                    displayGrid = int(val) == 1
    except:
        print 'Nu exista fisierul settings.cfg! Folosesc setarile implicite.'

    hCells = screenSize[0] // cellSize
    vCells = screenSize[1] // cellSize

    A = [[False for i in range(-9, vCells+9)] for j in range(-9, hCells+9)]
    pre = [[False for i in range(-9, vCells+9)] for j in range(-9, hCells+9)]

    i, j = 0, 0
    with open('initial-state.in', 'r') as f:
        for line in f:
            s = list(map(int, line.split()))
            for j in range(0, min(hCells-1, len(s))):
                A[j][i] = True if s[j] == 1 else False
                pre[j][i] = A[j][i]
            i += 1
            if i >= vCells:
                break

    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")

    screen = pygame.display.set_mode(screenSize, 0, 32)
    screen.fill(background)


def drawGrid():
    global screen, screenSize, displayGrid
    if not displayGrid:
        return

    for i in range(1, vCells+1):
        pygame.draw.line(
                screen,
                gridColor,
                (0, i*cellSize-1),
                (screenSize[0], i*cellSize-1)
                )
    for i in range(1, hCells+1):
        pygame.draw.line(
                screen,
                gridColor,
                (i*cellSize-1, 0),
                (i*cellSize-1, screenSize[1])
                )

    pygame.draw.line(screen, gridColor, (0, 0), (0, screenSize[1]))
    pygame.draw.line(screen, gridColor, (0, 0), (screenSize[0], 0))


def cell(i, j):
    return ((i*cellSize, j*cellSize), (cellSize-1, cellSize-1))


def paintCell(i, j, color):
    pygame.draw.rect(screen, color, cell(i, j))


def duplicate():
    global A, pre
    for x in range(-3, hCells+3):
        for y in range(-3, vCells+3):
            pre[x][y] = A[x][y]


def neighbours(x, y):
    global pre, ind
    return [pre[x + k[0]][y + k[1]] for k in ind].count(True)


def printMatrix(A):
    for x in range(0, hCells):
        for y in range(0, vCells):
            if A[x][y]:
                paintCell(x, y, cellColor)


def constructMatrix(A):
    for x in range(-7, hCells+7):
        for y in range(-7, vCells+7):
            k = neighbours(x, y)
            if k == 3:
                A[x][y] = True
            if k < 2 or k > 3:
                A[x][y] = False


def main():
    try:
        init()
    except:
        print 'Nu am putut face initializarea.'
        exit(0)

    print 'Dimensiunea: %i verticala, %i orizontala' % (vCells, hCells)

    while True:
        screen.fill(background)

        printMatrix(A)
        constructMatrix(A)
        drawGrid()

        pygame.display.flip()

        if A == pre or pygame.event.poll().type == pygame.QUIT:
            pygame.quit()
            break

        duplicate()
        time.sleep(secondsInbetween)


if __name__ == '__main__':
    main()
