from tkinter import (Frame, Canvas, Tk)

size = 400
letter, number = "HGFEDCBA", "12345678"


class board(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()
        self.makeGrid(size)
        self.showCoo()

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


# class piece():
#    def __init__(position)


def main():
    root = Tk()
    board(root)
    root.mainloop()


if __name__ == "__main__":
    print("Strating...")
    main()
