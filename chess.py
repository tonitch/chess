from tkinter import Frame, Canvas, Tk
from PIL import ImageTk, Image

size = 400
letter, number = "HGFEDCBA", "12345678"


class board(Frame):
    """
    class that represent the window
    """
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()
        self.makeGrid(size)
        self.showCoo()
        self.loadPieces()
        self.placeStart()

    def makeGrid(self, gridSize):
        """
        draw the grid in a canvas
        """
        self.gameGrid = Canvas(
            self,
            width=gridSize,
            height=gridSize,
            bg="black")

        self.gameGrid.grid(column=2, row=1)
        self.gameGrid.chessGrid = []
        for i in range(8):
            self.order = "12345678"
            if i % 2 == 0:
                self.order = self.order[::-1]
            self.gameGrid.chessGrid.append(self.order)
            for j in range(8):
                if int(self.gameGrid.chessGrid[i][j]) % 2 == 0:
                    self.gameGrid.create_rectangle(
                        i*size/8,
                        j*size/8,
                        (i+1)*size/8,
                        (j+1)*size/8,
                        fill="sandy brown")
                else:
                    self.gameGrid.create_rectangle(
                        i*size/8,
                        j*size/8,
                        (i+1)*size/8,
                        (j+1)*size/8,
                        fill="saddle brown")
        for i in range(1, 8):
            line = (gridSize/8)*i
            self.drawLine(line, 0, line, gridSize)
            self.drawLine(0, line, gridSize, line)
        self.gameGrid.bind("<Button-1>", self.touch)

    def placeStart(self):
        """
        place base pieces an create grid : self.piecesPositions
        """
        self.piecesPositions = []
        for i in range(8):
            self.piecesPositions.append(list())
            for j in range(8):
                self.piecesPositions[i].append('#')

        self.piecesPositions[0][0] = Piece(self, 0, 0, "black", 2)
        self.piecesPositions[0][1] = Piece(self, 1, 0, "black", 4)
        self.piecesPositions[0][2] = Piece(self, 2, 0, "black", 3)
        self.piecesPositions[0][3] = Piece(self, 3, 0, "black", 1)
        self.piecesPositions[0][4] = Piece(self, 4, 0, "black", 0)
        self.piecesPositions[0][5] = Piece(self, 5, 0, "black", 3)
        self.piecesPositions[0][6] = Piece(self, 6, 0, "black", 4)
        self.piecesPositions[0][7] = Piece(self, 7, 0, "black", 2)
        self.piecesPositions[1] = [Piece(self, i, 1, "black", 5) for i in range(8)]

        self.piecesPositions[7][0] = Piece(self, 0, 7, "white", 2)
        self.piecesPositions[7][1] = Piece(self, 1, 7, "white", 4)
        self.piecesPositions[7][2] = Piece(self, 2, 7, "white", 3)
        self.piecesPositions[7][3] = Piece(self, 3, 7, "white", 1)
        self.piecesPositions[7][4] = Piece(self, 4, 7, "white", 0)
        self.piecesPositions[7][5] = Piece(self, 5, 7, "white", 3)
        self.piecesPositions[7][6] = Piece(self, 6, 7, "white", 4)
        self.piecesPositions[7][7] = Piece(self, 7, 7, "white", 2)
        self.piecesPositions[6] = [Piece(self, i, 6, "white", 5) for i in range(8)]

        for i in range(8):
            print(self.piecesPositions[i])

    def showCoo(self):
        """
        draw coordinates around the board
        """
        self.cooL = Canvas(self, width=size/16, height=size, bg="gray")
        self.cooN = Canvas(self, width=size, height=size/16, bg="gray")
        self.cooL.grid(column=1, row=1)
        self.cooN.grid(column=2, row=2)
        for i in range(8):
            self.cooL.create_text(size/32, size/8*i+size/16, text=letter[i])
            self.cooN.create_text(size/8*i+size/16, size/32, text=number[i])

    def drawLine(self, x1, x2, y1, y2):
        """
        draw line with less info needed
        """
        self.gameGrid.create_line(x1, x2, y1, y2, width=2, fill="black")

    def loadPieces(self):
        """
        load Pieces to show them on the board with
        """
        self.Bpieces = []
        self.Wpieces = []
        self.img = Image.open("./images/chess_pieces.png")
        self.pieceSize = int(size/400*42)
        for x in range(6):
            self.Bpieces.append(
                ImageTk.PhotoImage(
                    self.img.crop((
                        x*128,
                        0,
                        (1+x)*128,
                        128)).resize((self.pieceSize, self.pieceSize))))
            self.Wpieces.append(
                ImageTk.PhotoImage(
                    self.img.crop((
                        x*128,
                        128,
                        (1+x)*128,
                        256)).resize((self.pieceSize, self.pieceSize))))

    def drawWhitePiece(self, x, y, piece):
        """
        draw white piece on the board
        """
        piece = self.gameGrid.create_image(x, y, image=self.Wpieces[piece])
        return piece

    def drawBlackPiece(self, x, y, piece):
        """
        draw black piece on the board
        """
        piece = self.gameGrid.create_image(x, y, image=self.Bpieces[piece])
        return piece

    def touch(self, event):
        gridX = int(8/size * event.x)
        gridY = int(8/size * event.y)
        if self.piecesPositions[gridY][gridX] is not "#":
            self.piecesPositions[gridY][gridX].move(5, 5)


class Piece():
    """
    class that represent a piece on the canvas
    """
    def __init__(self, board, x, y, team, type):
        self.board = board
        self.x = x
        self.y = y
        self.posX = x * size/8 + size/16
        self.posY = y * size/8 + size/16
        self.team = team
        self.type = type
        if self.team == "white":
            self.piece = self.board.drawWhitePiece(self.posX, self.posY, self.type)
        if self.team == "black":
            self.piece = self.board.drawBlackPiece(self.posX, self.posY, self.type)

    def __repr__(self):
        return str(self.type) + ";" + self.team[0]

    def move(self, x, y):
        """
        function to move a piece on the cavans
        """
        self.board.piecesPositions[self.y][self.x] = "#"

        self.x = x
        self.y = y
        self.posX = x * size/8 + size/16
        self.posY = y * size/8 + size/16

        self.board.piecesPositions[self.y][self.x] = self
        self.board.gameGrid.coords(self.piece, self.posX, self.posX)


def main():
    root = Tk()
    board(root).mainloop()


if __name__ == "__main__":
    print("Starting")
    main()
