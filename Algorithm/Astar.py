from Problem.state import State
from Problem.node import Node
from queue import PriorityQueue

def Astar(problem):
    node = Node(problem.initState)

    if problem.isGoal(node.state):
        return node.state.queens, [node.state.queens]

    frontier = PriorityQueue()
    frontier.put((problem.evaluation(node), node))

    reached = {}
    expand = []

    while not frontier.empty():
        print(frontier.qsize())
        node = frontier.get()[1]
        state = node.state

        if state.queens not in expand:
            expand.append(state.queens)

        if problem.isGoal(state):
            return state.queens, expand

        for child in problem.successor(node):
            state = child.state
            fChild = problem.evaluation(child)
            
            if (state not in reached) or (fChild < problem.evaluation(problem, reached[state])):
                reached[state] = child
                frontier.put((fChild, child))

    return [], []