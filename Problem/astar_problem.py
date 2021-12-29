from Algorithm.Astar import Astar
from Problem.node import Node
from Problem.state import State
import os
import random

class AstarProblem:
    def __init__(self, size:int=0, initQueens:list=[]) -> None:
        self.size = size
        self.initState = State(initQueens)

    def isGoal(self, state:State) -> bool:
        if len(state.queens) != self.size:
            return False
        for i in range(len(state.queens)):
            for j in range(i+1, len(state.queens)):
                if self.isAttack(state.queens[i], state.queens[j]):
                    return False
        return True

    def isAttack(self, pos_queen1:int, pos_queen2:int) -> bool:
        row_queen1 = (pos_queen1 - 1) // self.size
        col_queen1 = (pos_queen1 - 1) %  self.size
        row_queen2 = (pos_queen2 - 1) // self.size
        col_queen2 = (pos_queen2 - 1) %  self.size

        if row_queen1 == row_queen2: return True
        if col_queen1 == col_queen2: return True
        if (row_queen1 + col_queen1) == (row_queen2 + col_queen2): return True
        if (row_queen1 - col_queen1) == (row_queen2 - col_queen2): return True
        return False

    def successor(self, node:Node) -> list:
        childs = []

        if len(node.state.queens) == self.size:
            return childs

        board = node.state.generateBoard(self.size)

        # print(node.state.queens)
        # s = ""
        # for r in range(self.size):
        #     for c in range(self.size):
        #         if board[r][c]:
        #             s += "Q  "
        #         else:
        #             s += "_  "
        #     s += '\n'
        # print(s)
        # os.system('pause')

        # for row in range(self.size):
        #     for col in range(self.size):
        #         if board[row][col] == True:
        #             queens = node.state.queens.copy()
        #             queens.append(row * self.size + col + 1)
        #             state = State(queens)
        #             path_cost = self.cost_function(node.state, state) + node.path_cost
        #             childNode = Node(state, path_cost, node)
        #             childs.append(childNode)

        for row in range(self.size):
            for col in range(self.size):
                if (row*self.size + col + 1) not in node.state.queens:
                    queens = node.state.queens.copy()
                    queens.append(row * self.size + col + 1)
                    state = State(queens)
                    path_cost = self.cost_function(node.state, state) + node.path_cost
                    childNode = Node(state, path_cost, node)
                    childs.append(childNode)

        return childs

    def evaluation(self, node:Node) -> int:
        return node.path_cost + self.heuristic(node.state)

    def cost_function(self, pre_state:State, state:State) -> int:
        # # num_queen_attack = 0
        # # for i in range(0, len(state.queens)):
        # #     for j in range(i+1, len(state.queens)):
        # #         if self.isAttack(state.queens[i], state.queens[j]):
        # #             num_queen_attack += 1
        # # return len(state.queens) + num_queen_attack
        # return self.size - len(state.queens)
        return 1

    def heuristic(self, state:State) -> int:
        num_queen_attack = 0
        for i in range(0, len(state.queens)):
            for j in range(i+1, len(state.queens)):
                if self.isAttack(state.queens[i], state.queens[j]):
                    num_queen_attack += 1
        return num_queen_attack

    def solve(self):
        return Astar(self)