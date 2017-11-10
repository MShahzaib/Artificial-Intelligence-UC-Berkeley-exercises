# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def getDirections(path):
    Dir = []
    for x in path:
        Dir.append(x[1])
    Dir.pop(0)
    return Dir


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""

    visted_states = set()
    fringe = util.Stack()

    current_state = problem.getStartState()
    Start_Node = [(current_state,'South', 0)]
    fringe.push(Start_Node) 


    while True:
        if (fringe.isEmpty()):
            raise Exception("solution not available")
            break

        current_node = fringe.pop()
        last_state_of_path = current_node[-1][0]

        if (problem.isGoalState(last_state_of_path)):
            return getDirections(current_node)
        else:
            if (not (last_state_of_path in visted_states)):
                visted_states.add(last_state_of_path)
                next_states = problem.getSuccessors(last_state_of_path)
                for n_s in next_states:
                    new_node = list(current_node)
                    new_node.append(n_s)
                    fringe.push(new_node)
        
             
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    visted_states = set()
    fringe = util.PriorityQueue()

    current_state = problem.getStartState()
    Start_Node = [(current_state,'', 0)]
    fringe.push(Start_Node,0) 

    while True:
        if (fringe.isEmpty()):
            raise Exception("solution not available")
            break

        current_node = fringe.pop()
        last_state_of_path = current_node[-1][0]

        if (problem.isGoalState(last_state_of_path)):
            return getDirections(current_node)
        else:
            if (not (last_state_of_path in visted_states)):
                visted_states.add(last_state_of_path)
                next_states = problem.getSuccessors(last_state_of_path)
                for n_s in next_states:
                    new_node = list(current_node)
                    new_node.append(n_s)
                    fringe.push(new_node,len(new_node))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    visted_states = set()
    fringe = util.PriorityQueue()

    current_state = problem.getStartState()
    Start_Node = [(current_state,'', 0)]
    fringe.push(Start_Node,0) 

    while True:
        if (fringe.isEmpty()):
            raise Exception("solution not available")
            break

        current_node = fringe.pop()
        last_state_of_path = current_node[-1][0]

        if (problem.isGoalState(last_state_of_path)):
            return getDirections(current_node)
        else:
            if (not (last_state_of_path in visted_states)):
                visted_states.add(last_state_of_path)
                next_states = problem.getSuccessors(last_state_of_path)
                for next_state in next_states:
                    new_node = list(current_node)
                    next_state_list = list(next_state)
                    next_state_list[2] += new_node[-1][2]
                    new_node.append(tuple(next_state_list))
                    fringe.push(new_node,next_state_list[2])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    visted_states = set()
    fringe = util.PriorityQueue()

    current_state = problem.getStartState()
    Start_Node = [(current_state,'', 0)]
    fringe.push(Start_Node,0) 

    while True:
        if (fringe.isEmpty()):
            raise Exception("solution not available")
            break

        current_node = fringe.pop()
        last_state_of_path = current_node[-1][0]

        if (problem.isGoalState(last_state_of_path)):
            return getDirections(current_node)
        else:
            if (not (last_state_of_path in visted_states)):
                visted_states.add(last_state_of_path)
                next_states = problem.getSuccessors(last_state_of_path)
                for next_state in next_states:
                    new_node = list(current_node)
                    next_state_list = list(next_state)
                    next_state_list[2] += new_node[-1][2]
                    new_node.append(tuple(next_state_list))
                    fringe.push(new_node,next_state_list[2] + heuristic(next_state_list[0],problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
