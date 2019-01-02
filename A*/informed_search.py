# -----------------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Implement astar and some heuristics
#
# Author: Itaru Kishikawa
#
# -----------------------------------------------------------------------------
"""
A* Algorithm and heuristics implementation 

Your task for homework 3 is to implement:
1.  astar
2.  single_heuristic 
3.  better_heuristic
4.  gen_heuristic  
"""
import data_structures


def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    # Enter your code here and remove the pass statement below
    closed = set()  # keep track of our explored states
    fringe = data_structures.PriorityQueue()  # for aster, the fringe is a priority queue
    state = problem.start_state()
    root = data_structures.Node(state)
    fringe.push(root, 0)
    while True:
        if fringe.is_empty():
            return None  # Failure - fringe is empty and no solution was found
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node.solution()
        if node.state not in closed:  # we are implementing graph search
            closed.add(node.state)
            for child_state, action, action_cost in problem.successors(
                    node.state):
                child_node = data_structures.Node(child_state, node, action, node.cumulative_cost + action_cost)
                fringe.push(child_node, child_node.cumulative_cost + heuristic(child_state, problem))


def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*. 
    Running A* with this null heuristic, gives us uniform cost search
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def single_heuristic(state, problem):
    """
    Based on the Manhattan distance.
    We assume there is only one medal in the quest.
    Assume there is no wall.
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return: heuristic value
    """
    # Enter your code here and remove the pass statement below
    x1, y1 = state[0]
    x2, y2 = list(problem.medals)[0]
    return abs(x1 - x2) + abs(y1 - y2)


def h(start, goal):
    x1, y1 = start
    x2, y2 = goal
    x_sum = abs(x1 - x2)
    y_sum = abs(y1 - y2)
    x_sum *= 1 if x1 < x2 else 2
    y_sum *= 1 if y1 > y2 else 6
    return x_sum + y_sum


def better_heuristic(state, problem):
    """
    Return move cost based on Manhattan distance.
    Heuristics use some domain knowledge and are problem specific.
    Assume there is only one medal in the quest.
    Assume there is no wall and count the each cost of move
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest 
    :return: heuristic value
    """
    # Enter your code here and remove the pass statement below
    return h(state[0], list(problem.medals)[0])


def gen_heuristic(state, problem):
    """
    The maze contains an arbitrary number of medals and
    these medals can be anywhere in the maze.
    Assume there is no wall and count the each cost of move
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest 
    :return: heuristic value
    """
    # Enter your code here and remove the pass statement below
    start = state[0]
    medals = state[1]
    lst = []
    for medal in medals:
        lst.append(h(start, medal))

    return 0 if len(lst) == 0 else max(lst)
