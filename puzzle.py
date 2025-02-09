import heapq as min_heap
import copy
import time

#directly from the example report 
def main():
    puzzle_mode = input("Welcome to Ashley's puzzle solver. Type '1' to use a default puzzle, or '2' to create your own \n")
    if puzzle_mode == '1':
        #select algo chooses between: uniform, misplaced, manhattan
        #default puzzles are the different difficulty of puzzles
        puzzle = default_puzzles()
        heuristic = input("Select algorithm. (1) uniform cost search (2) A* Misplaced Tile Heuristic (3) A* Manhattan Distance Heuristic \n")
        a_star_search(puzzle, heuristic)

    if puzzle_mode == '2':
        print("Enter your puzzle, using zero to represent the blank. Only enter valid 8-puzzles. Separate the numbers with a SPACE and press RET when finished")
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")

        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()

        for i in range (0,3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])

        user_puzzle = (puzzle_row_one, puzzle_row_two, puzzle_row_three)
        user_puzzle = tuple(map(tuple, user_puzzle))
        print(user_puzzle)
        heuristic = input("Select algorithm. (1) uniform cost search (2) A* Misplaced Tile Heuristic (3) A* Manhattan Distance Heuristic \n")
        a_star_search(user_puzzle, heuristic)
    return

#https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288 heavily referenced
def a_star_search(state, heuristic):  
#need to evaluate which state is the most promising 
#f = cost + estimated cost 
    start_time = time.time()
    starting_node = Puzzle(state)
    starting_node.cost = select_algo(state, heuristic)
    working_queue = []
    repeated_states = set()
    min_heap.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    #need to use tuple so we can insert lists to our repeated_states
    repeated_states.add(tuple(map(tuple, starting_node.state)))

    #expand nodes until we reach goal state or queue is empty
    while len(working_queue) > 0: 
            
        max_queue_size = max(len(working_queue), max_queue_size)
        node_from_queue = min_heap.heappop(working_queue)

        if time.time() - start_time > 300: #run for only 5 minutes, we dont want this to last forever
            print("We have run out of time")
            print("Number of nodes expanded: ", num_nodes_expanded)
            print("Max queue size: ", max_queue_size)
            print('Solution depth: ', node_from_queue.depth)
            return None

        if node_from_queue.state == goalState: #we fixed the puzzle
            print("Number of nodes expanded: ", num_nodes_expanded)
            print("Max queue size: ", max_queue_size)
            print('Solution depth: ', node_from_queue.depth)
            print("Time: ", time.time() - start_time) 
            return node_from_queue

        num_nodes_expanded +=1
        print("The best state to expand with a g(n) = " + str(node_from_queue.depth) + " and h(n) = " + str(node_from_queue.cost) +" is...")
        print_puzzle(node_from_queue.state)
        for child in expand(node_from_queue): #run the heuristic on the children to see which is best 
            child = tuple(map(tuple, child)) #convert state
            if child not in repeated_states: #check if we've seen it already
                repeated_states.add(child)  #add if its new 
                child_puzzle = Puzzle(child)
                child_puzzle.depth = node_from_queue.depth + 1
                child_puzzle.cost = child_puzzle.depth + select_algo(child_puzzle.state, heuristic)
                min_heap.heappush(working_queue, child_puzzle) #push child into our queue

#for the main menu, directly from the code provided 
def select_algo(puzzle, algorithm):
    if algorithm == '1':
        return uniform_cost_search(puzzle)
    if algorithm == '2':
        return misplaced_tile(puzzle)
    if algorithm == '3':
        return manhattan_heuristic(puzzle)

#directly from the code provided
def default_puzzles():
    difficulty = input(
        "Please enter a desired difficulty on a scale from 0 to 6. \n")
    if difficulty == '0':
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if difficulty == '1':
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    if difficulty == '2':
        print("Difficulty of 'Easy' selected.")
        return easy
    if difficulty == '3':
        print("Difficulty of 'Medium' selected.")
        return medium
    if difficulty == '4':
        print("Difficulty of 'Hard' selected.")
        return hard
    if difficulty == '5':
        print("Difficulty of 'Very Hard' selected.")
        return veryHard
    if difficulty == '6':
        print("Difficulty of 'Impossible' selected.")
        return impossible
    

def print_puzzle(puzzle):
    for i in range(0,3):
        print(puzzle[i])
    print('\n')


#default puzzle options
trivial = ((1, 2, 3),
(4, 5, 6),
(7, 8, 0))

veryEasy = [[1, 2, 3],
[4, 5, 6],
[0, 7, 8]]

easy = [[1, 2, 0],
[4, 5, 3],
[7, 8, 6]]

medium = [[0, 1, 2],
[4, 5, 3],
[7, 8, 6]]

hard = [[8, 7, 1],
[6, 0, 2],
[5, 4, 3]]

#https://w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/ very hard state here
#requires at least 31 moves to solve 
veryHard = [[8, 6, 7],
[2, 5, 4],
[3, 0, 1]]

#https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
#impossible state cited from ^
impossible = [[8, 1, 2],
[0, 4, 3],
[7, 6, 5]]

#compare this to every state to see if the puzzle is finished 
goalState = ((1, 2, 3), 
             (4, 5, 6), 
             (7, 8, 0))
  
#find where we want this value to be 
def goal_pos(goalState, state): 
    for i in range(3): #x axis
        for j in range (3): #y axis 
            if goalState[i][j] == state: 
                return i, j

def manhattan_heuristic(state):
    #check the current state and see how far each value is from the goal 
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0: #skip 0 
                goal_row, goal_column = goal_pos(goalState, state[i][j]) #find where we should be 
                distance += abs(i - goal_row) + abs(j - goal_column) #compare how far our goal is to our current pos 
    return distance

def misplaced_tile(state):
    #count which tiles are not in its goal state
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0: #skip the 0
                if(goalState[i][j] != state[i][j]): #if the correct place is not the same as our spot its misplaced
                    count += 1
    return count

#provides no heuristic for the search to work with 
def uniform_cost_search(puzzle):
    return 0

#class to define each puzzle state 
class Puzzle:
    def __init__(self, state, parent = None, depth = 0, cost = 0):
        self.state = state
        self.depth = depth
        self.cost = cost
    #compare puzzles in our queue
    def __lt__(self, other):
        return self.cost < other.cost

    #to help track duplicate states 
    def __eq__(self, other):
        return self.state == other.state

#find the possible children and choose one
def expand(puzzle):
    children = []
#find where the zero is first 
    zero_row = 0
    zero_col = 0
    for i in range(3):
        for j in range (3):
            if puzzle.state[i][j] == 0:
                zero_row = i
                zero_col = j
#check each possible move, up, down, left, right 
#then we need to change the puzzle to move for viable option -> this becomes the children  
    if zero_row > 0: #move down
        children.append(move(puzzle.state, zero_row - 1, zero_col, zero_row, zero_col))
    if zero_row < 2: #move up 
        children.append(move(puzzle.state, zero_row + 1, zero_col, zero_row, zero_col))
    if zero_col > 0: #move left
        children.append(move(puzzle.state, zero_row, zero_col - 1, zero_row, zero_col))
    if zero_col < 2: #move right
        children.append(move(puzzle.state, zero_row, zero_col + 1, zero_row, zero_col))
    return children

#create a copy of existing state and swap the values
def move(state, new_row, new_col, old_row, old_col):
    child = copy.deepcopy(state)
    child_list = list(map(list, child)) #convert tuple -> list 
    child_list[old_row][old_col] = child_list[new_row][new_col] #swap coordinates
    child_list[new_row][new_col] = 0 
    child = tuple(map(tuple, child_list)) #convert back to tuple
    return child


main()

#Sources:
#https://w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/ very hard state 
#https://www.geeksforgeeks.org/8-puzzle-problem-in-ai/  heuristics references 
#https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/ example states 
#https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288 reference for search algorithm
#https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/ tuples vs list in a set 
#https://www.dropbox.com/scl/fi/c9bh5abkogqab8kdpcwv9/Project_1_The_Eight_Puzzle_CS_170_2025.pdf?rlkey=7pzohokhogxs4ezauidw7f753&e=1&dl=0 heavily referenced guide that professor eamonn posted 