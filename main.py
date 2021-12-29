from visual import chessBoard, chessGame
import os
from program import Program
from Problem.astar_problem import AstarProblem

if __name__=='__main__':
    problem = AstarProblem(4, [])
    solution = problem.solve()
    print(solution)

    '''
    os.system("cls")
    print("1. CNF file input")
    print("2. A* file input")
    print("3. Click on chess board to input queen")
    option = input("Choose option:  ")

    program = Program(8)
    
    if option == "1":
        os.system("cls")
        # all file in INPUT folder
        INPUT_DIR = './Input/cnf'
        files = [name.replace('.txt', '') for name in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, name))]

        print('Available input files: ', end='  ')
        sFile = ''
        for file in files:
            sFile += file + '    '
        print(sFile)

        inputValid = False
        while not inputValid:
            file = input("Enter filename: ")
            inputValid = program.InputCNF(filename=file)

        program.solveCNF()
        print("Level 1:  ", program.cnf_solution1[0])
        print("CNF: ", program.cnf_solution1[2])
        print("Level 2:  ", program.cnf_solution2[0])
        print("CNF: ", program.cnf_solution2[2])

        step1 = program.cnf_solution1[1]
        step2 = program.cnf_solution2[1]
        chessBoard(program.numQueen, step1, "CNF level 1")
        chessBoard(program.numQueen, step2, "CNF level 2")
    elif option == "2":
        os.system("cls")
        # all file in INPUT folder
        INPUT_DIR = './Input/astar'
        files = [name.replace('.txt', '') for name in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, name))]

        print('Available input files: ', end='  ')
        sFile = ''
        for file in files:
            sFile += file + '    '
        print(sFile)

        inputValid = False
        while not inputValid:
            file = input("Enter filename: ")
            inputValid = program.InputAstar(filename=file)

        program.solveAstar()

        chessBoard(program.numQueen, program.astar_expand)
    elif option == "3":
        chessGame(program)
    '''
    