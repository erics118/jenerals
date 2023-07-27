from cmu_graphics import *
from objects.board import drawBoard
# drawImage("../assets/city.png", 100, 100)


def onAppStart(app):
    # grid
    app.rows = 20
    app.cols = 20
    app.boardLeft = 50
    app.boardTop = 50
    app.boardWidth = 500
    app.boardHeight = 500
    app.cellBorderWidth = 1

    app.cellWidth = app.boardWidth / app.cols
    app.cellHeight = app.boardHeight / app.rows

# [[None] * app.cols for _ in range(app.rows)]
    app.board = [[None, 'mountain'] * (app.cols//2) for _ in range(app.rows)]


def redrawAll(app):
    
    drawBoard(app)



runApp(width=600, height=600)
