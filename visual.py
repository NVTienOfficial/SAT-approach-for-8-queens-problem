import pygame

from program import Program

SQ_SIZE = 64
MAX_FPS = 15
IMAGE = {}

def loadImage():
    IMAGE['queen'] = pygame.transform.scale(pygame.image.load("queen.png"), (SQ_SIZE, SQ_SIZE))

def drawGameState(screen:pygame.Surface, queens, size):
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((size/2-1)*SQ_SIZE, size*SQ_SIZE + 25, 2*SQ_SIZE, SQ_SIZE))
    font = pygame.font.SysFont('didot.ttc', 40)
    GREEN = (0, 255, 0)
    img = font.render('SOLVE', True, GREEN)
    screen.blit(img, ((size/2-1)*SQ_SIZE + 15, size*SQ_SIZE + 45))
    drawBoard(screen, size)
    drawPieces(screen, queens)

def drawBoard(screen, size:int = 8):
    colors = [pygame.Color("white"), pygame.Color("grey")]
    for row in range(size):
        for col in range(size):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen:pygame.Surface, queens):
    for q in queens:
        screen.blit(IMAGE['queen'], pygame.Rect(q[1]*SQ_SIZE, q[0]*SQ_SIZE, SQ_SIZE, SQ_SIZE))            

def chessGame(program:Program):
    loadImage()
    pygame.init()
    size = program.numQueen
    screen = pygame.display.set_mode((size*SQ_SIZE, size*SQ_SIZE+100))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("black"))
    running = True
    queens = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[1] >= size*SQ_SIZE + 25 and pos[1] <= (size+1)*SQ_SIZE + 25 and pos[0] >= (size/2-1)*SQ_SIZE and pos[0] <= (size/2-1)*SQ_SIZE + 2*SQ_SIZE:
                    program.position = queens
                    program.solveAstar()
                    print(program.astar_solution)
                    queens = program.indexToPosition(program.astar_solution)
                elif len(queens) < size and pos[1] < size*SQ_SIZE:
                    col = pos[0] // SQ_SIZE
                    row = pos[1] // SQ_SIZE
                    queens.append([row, col])
        
        drawGameState(screen, queens, size)
        clock.tick(MAX_FPS)
        pygame.display.flip()


def chessBoard(size:int, idx:list, title:str):
    loadImage()
    pygame.init()
    screen = pygame.display.set_mode((size*SQ_SIZE, size*SQ_SIZE+100))
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("black"))
    running = True
    step = []
    for i in idx:
        hold = [[(pos-1) // size, (pos - 1) % size] for pos in i]
        step.append(hold)
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if i == len(step):
            i -= 1
        drawGameState(screen, step[i], size)
        i += 1
        clock.tick(5)
        pygame.display.flip()