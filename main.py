from tkinter import Frame, Canvas, Tk
from PIL import ImageTk, Image
import time

size = 400
letter, number = "HGFEDCBA", "12345678"


class board(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()
        self.makeGrid(size)
        self.showCoo()
        self.loadPieces()

    def makeGrid(self, gridSize):
        self.gameGrid = Canvas(
            self,
            width=gridSize,
            height=gridSize,
            bg="darkgray")

        self.gameGrid.grid(column=2, row=1)
        for i in range(1, 8):
            line = (gridSize/8)*i
            self.drawLine(line, 0, line, gridSize)
            self.drawLine(0, line, gridSize, line)

    def showCoo(self):
        self.cooL = Canvas(self, width=size/16, height=size, bg="gray")
        self.cooN = Canvas(self, width=size, height=size/16, bg="gray")
        self.cooL.grid(column=1, row=1)
        self.cooN.grid(column=2, row=2)
        for i in range(8):
            self.cooL.create_text(size/32, size/8*i+size/16, text=letter[i])
            self.cooN.create_text(size/8*i+size/16, size/32, text=number[i])

    def drawLine(self, x1, x2, y1, y2):
        self.gameGrid.create_line(x1, x2, y1, y2, width=2, fill="gray")

    def loadPieces(self):
        self.Bpieces = []
        self.Wpieces = []
        self.img = Image.open("./images/chess_pieces.png")
        for x in range(6):
            self.Bpieces.append(
                ImageTk.PhotoImage(
                    self.img.crop((
                        x*128,
                        0,
                        (1+x)*128,
                        128)).resize((42, 42))))
            self.Wpieces.append(
                ImageTk.PhotoImage(
                    self.img.crop((
                        x*128,
                        128,
                        (1+x)*128,
                        256)).resize((42, 42))))

    def drawWhitePiece(self, x, y, piece):
        piece = self.gameGrid.create_image(x, y, image=self.Wpieces[piece])
        return piece

    def drawBlackPiece(self, x, y, piece):
        piece = self.gameGrid.create_image(x, y, image=self.Bpieces[piece])
        return piece


class Piece():
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
        self.board.gameGrid.move(self.piece, x, y)


def main():
    root = Tk()
    myboard = board(root)
    p = Piece(myboard, 100, 100, "white", 1)
    print(p.piece)
    p.move(0,0)
    root.mainloop()


if __name__ == "__main__":
    print("Starting")
    main()
