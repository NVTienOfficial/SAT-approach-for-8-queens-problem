import os
from Problem.cnf_problem import CNFProblem
from Problem.astar_problem import AstarProblem

class Program:
    def __init__(self, n:int) -> None:
        self.numQueen = n

    def solveCNF(self):
        self.cnf_problem = CNFProblem(self.numQueen, self.clause)
        self.cnf_solution1 = self.cnf_problem.solveLevel1()
        self.cnf_solution2 = self.cnf_problem.solveLevel2()

    def solveAstar(self):
        self.astar_problem = AstarProblem(self.numQueen, self.positionToIndex(self.position))
        self.astar_solution, self.astar_expand = self.astar_problem.solve()

    def InputCNF(self, filename):
        filename += ".txt"
        if os.path.isfile(os.path.join('./Input/cnf', filename)):
            self.finput = filename.replace(".txt", "")
            filepath = os.path.join('./Input/cnf', filename)
            N, clause = self.readFileCNF(filepath)
            if N != None and clause != None:
                self.size = N
                self.clause = clause
                return True
        print('Invalid filename')
        return False

    def readFileCNF(self, filepath):
        if not os.path.exists(filepath):
            return None, None
        
        file = open(filepath, "r")

        N = (int)(file.readline())
        cnf = []
        for _ in range(N):
            line = file.readline()
            tmp = line.split(' ')
            if len(tmp) == 2:
                cor = [int(x) for x in tmp]
                cnf.append([cor[0]*self.numQueen + cor[1] + 1])
            elif len(tmp) == 3:
                cor = [int(tmp[i]) for i in range(1, len(tmp))]
                cnf.append([-(cor[0]*self.numQueen + cor[1] + 1)])

        file.close()
        return N, cnf

    def InputAstar(self, filename):
        filename += ".txt"
        if os.path.isfile(os.path.join('./Input/astar', filename)):
            self.finput = filename.replace(".txt", "")
            filepath = os.path.join('./Input/astar', filename)
            N, pos = self.readFileAStar(filepath)
            if N != None and pos != None:
                self.size = N
                self.position = pos
                return True
        print('Invalid filename')
        return False

    def readFileAStar(self, filepath):
        if not os.path.exists(filepath):
            return None, None
        
        file = open(filepath, "r")

        N = (int)(file.readline())
        queens = []
        for _ in range(N):
            line = file.readline()
            tmp = line.split(' ')
            queen = [int(x) for x in tmp]
            queens.append(queen)

        file.close()
        return N, queens

    def positionToIndex(self, position:list):
        return [(pos[0] * self.numQueen + pos[1] + 1) for pos in position]
    
    def indexToPosition(self, idx:list):
        position = []
        for i in idx:
            row = (i - 1) // self.numQueen
            col = (i - 1) % self.numQueen
            position.append([row, col])
        return position