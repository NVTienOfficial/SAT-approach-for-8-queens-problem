import random

class State:
    def __init__(self, queens:list=[]) -> None:
        self.queens = queens

    def generateBoard(self, n:int):
        board = [[True for _ in range(n)] for _ in range(n)]
        for q in self.queens:
            row = (q - 1) // n
            col = (q - 1) % n
            
            for i in range(n):
                board[i][col] = False
                board[row][i] = False

            i = 1
            while row-i >= 0 and col-i >= 0:
                board[row-i][col-i] = False
                i += 1
            
            i = 1
            while row+i < n and col+i < n:
                board[row+i][col+i] = False
                i += 1

            i = 1
            while row-i >= 0 and col+i < n:
                board[row-i][col+i] = False
                i += 1

            i = 1
            while row+i < n and col-i >= 0:
                board[row+i][col-i] = False
                i += 1

        return board

    def toString(self):
        s = ""
        for p in self.pos:
            s += str(p)
        return s