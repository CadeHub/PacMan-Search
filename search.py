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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #initialize stack and visited list
    st = util.Stack()                   #initialize stack 
    visited = []

    #push inital state onto stack, and add it to visited list
    st.push((problem.getStartState(), None, None))                  #FORMAT: ((x, y), action, parent)
    visited.append(problem.getStartState())
    while not st.isEmpty():                
        node = st.pop()
        visited.append(node[0])
        print("popped: ", node)
    
        #check if this node is goal, if so return epic path
        if problem.isGoalState(node[0]):
            solutionPath = []
            solutionPath.extend(node[2])
            solutionPath.append(node[1])
            return solutionPath

        
        #build parent path to store in successors
        parentPath = []
        if problem.getStartState() != node[0]:
            parentPath.extend(node[2])
            parentPath.append(node[1])

        #if not goal, add (nonvisited) successors to stack
        succ = []
        succ = problem.getSuccessors(node[0])

        for i in succ:
            if i[0] not in visited:
                st.push((i[0],i[1],parentPath))
                



    print("exited loop failstate")
    return "f"
    
    
        

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    #initialize stack and visited list
    qu = util.Queue()                   #initialize stack 
    visited = []

    #push inital state onto stack, and add it to visited list
    qu.push((problem.getStartState(), None, None))                  #FORMAT: ((x, y), action, parent)
    visited.append(problem.getStartState())

    while not qu.isEmpty():                
        node = qu.pop()
        #check if this node is goal, if so return epic path
        if problem.isGoalState(node[0]):
            solutionPath = []
            solutionPath.extend(node[2])
            solutionPath.append(node[1])
            return solutionPath

        #build parent path to store in successors
        parentPath = []
        if problem.getStartState() != node[0]:
            parentPath.extend(node[2])
            parentPath.append(node[1])

        #if not goal, add (nonvisited) successors to stack
        succ = []
        succ = problem.getSuccessors(node[0])
        for i in succ:
            if i[0] not in visited:
                qu.push((i[0],i[1],parentPath))
                visited.append(i[0])

    print("exited loop failstate")
    return "f"

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    #initialize Queue and visited list, and add initial state to it
    qu = util.PriorityQueue()
    visited = []
    qu.push((problem.getStartState(), None, None), 1)  #FORMAT: (priorityQueue?, node, priority)
    visited.append(problem.getStartState())
    while not qu.isEmpty():  
        #pop first item off Queue              
        node = qu.pop()
        #print("Current Node = ", node[0])


        #check if this node is goal, if so return epic path
        if problem.isGoalState(node[0]):
            solutionPath = node[2]
            solutionPath.append(node[1])
            return solutionPath

        #if not goal, add (nonvisited) successors to Queue

        #setup parentPath
        parentPath = []
        #if start state than ignore parentPath setup (because there isn't one)
        if problem.getStartState() != node[0]:
            parentPath.extend(node[2])
            parentPath.append(node[1])

        #if not goal, add (nonvisited) successors to Queue
        succ = problem.getSuccessors(node[0])
        #print("Adding Successors: ")
        for i in succ:
            if i[0] not in visited:
                qu.push((i[0],i[1],parentPath),i[2])
                visited.append(i[0])


    print("Exited Loop, no path found")
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #initialize Queue and visited list, and add initial state to it
    qu = util.PriorityQueue()
    visited = []
    qu.push((problem.getStartState(), None, None), 1)  #FORMAT: (priorityQueue?, node, priority)
    visited.append(problem.getStartState())
    while not qu.isEmpty():  
        #pop first item off Queue              
        node = qu.pop()
        #print("Current Node = ", node[0])

        #mark (just the coordinates) as visited
        visited.append(node[0])

        #check if this node is goal, if so return epic path
        if problem.isGoalState(node[0]):
            solutionPath = node[2]
            solutionPath.append(node[1])
            return solutionPath

        #if not goal, add (nonvisited) successors to Queue

        #setup parentPath
        parentPath = []
        #if start state than ignore parentPath setup (because there isn't one)
        if problem.getStartState() != node[0]:
            parentPath.extend(node[2])
            parentPath.append(node[1])

        #if not goal, add (nonvisited) successors to Queue
        succ = problem.getSuccessors(node[0])
        #print("Adding Successors: ")
        for i in succ:
            if i[0] not in visited:
                qu.push((i[0],i[1],parentPath),i[2] + heuristic(i[0], problem()))
                visited.append(i[0])


    print("Exited Loop, no path found")
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
