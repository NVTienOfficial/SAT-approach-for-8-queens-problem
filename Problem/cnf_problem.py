from Algorithm.cnf import SatSolver
import random

class CNFProblem:
    def __init__(self, n:int = 8, init:list = []) -> None:
        self.size = n
        self.initCNF = init

    def index(self, row:int, col:int):
        return row*self.size + col + 1

    def getRow(self, idx:int):
        return (idx - 1) // self.size

    def getCol(self, idx: int):
        return (idx - 1) % self.size

    def solveLevel1(self):
        cnf = self.initCNF

        case = []
        row = [random.randint(0, self.size-1)*self.size + c + 1 for c in range(self.size)]
        while len(case) < pow(self.size, self.size):
            while row in case:
                row = [random.randint(0, self.size-1)*self.size + c + 1 for c in range(self.size)]
            case.append(row)

            hold = cnf.copy()
            for i in range(len(row)):
                hold = add(self.queenCNF((row[i]-1) // self.size, i), hold)

            solution = SatSolver(hold)
            if solution != [] or len(solution) == self.size:
                return solution, case, cnf

        return [], None, cnf

    def solveLevel2(self):
        cnf = self.initCNF
        cnf = add(self.attackCNF(), cnf)

        for i in range(self.size):
            cnf.append([self.index(i,c) for c in range(self.size)])
            cnf.append([self.index(r,i) for r in range(self.size)])

        solution = SatSolver(cnf)
        if solution != [] or len(solution) == self.size:
            return solution, [solution], cnf

        return [], None, cnf

    def getCase(self):
        queens = []
        for _ in range(self.size):
            q = random.randint(0, self.size*self.size - 1)
            while q in queens:
                q = random.randint(0, self.size*self.size - 1)
            queens.append(q)
        return queens

    def queenCNF(self, row:int, col:int):
        cnf = [[self.index(row,col)]]

        for r in range(self.size):
            if r != row:
                cnf.append([-self.index(r, col)])

        for c in range(self.size):
            if c != col:
                cnf.append([-self.index(row, c)])

        i = 1
        while row-i >= 0 and col-i >= 0:
            cnf.append([-self.index(row-i, col-i)])
            i += 1

        i = 1
        while row+i < self.size and col+i < self.size:
            cnf.append([-self.index(row+i, col+i)])
            i += 1

        i = 1
        while row-i >= 0 and col+i < self.size:
            cnf.append([-self.index(row-i, col+i)])
            i += 1

        i = 1
        while row+i < self.size and col-i >= 0:
            cnf.append([-self.index(row+i, col-i)])
            i += 1

        return cnf

    def attackCNF(self):
        cnf = []

        for r in range(self.size):
            for c in range(self.size):
                v = self.index(r,c)

                i = 1
                while c + i < self.size:
                    cnf.append([-v, -self.index(r, c+i)])
                    i += 1

                i = 1
                while r + i < self.size:
                    cnf.append([-v, -self.index(r+i, c)])
                    i += 1

                i = 1
                while r + i < self.size and c + i < self.size:
                    cnf.append([-v, -self.index(r+i, c+i)])
                    i += 1

                i = 1
                while r + i < self.size and c - i >= 0:
                    cnf.append([-v, -self.index(r+i, c-i)])
                    i += 1

        return cnf

def add(src:list, dest:list) -> list:
    for i in src:
        dest.append(i)
    return dest