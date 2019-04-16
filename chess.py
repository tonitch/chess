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
        self.mainloop()

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


class Piece():
    """
    class that represent a piece on the canvas
    """
    def __init__(self, board, x, y, team, type):
        self.board = board
        self.x = x
        self.y = y
        self.team = team
        self.type = type
        if self.team == "white":
            self.piece = self.board.drawWhitePiece(self.x, self.y, self.type)
        if self.team == "black":
            self.piece = self.board.drawBlackPiece(self.x, self.y, self.type)

    def move(self, x, y):
        """
        function to move a piece on the cavans
        """
        self.board.gameGrid.coords(self.piece, x, y)


def main():
    root = Tk()
    board(root)


if __name__ == "__main__":
    print("Starting")
    main()
