import heapq as min_heap_esque_queue

def main():
    puzzle_mode = input("Welcome to Ashley's puzzle solver. Type '1' to use a default puzzle, or '2' to create your own \n")

    if puzzle_mode == 1:
        #select algo chooses between: uniform, misplaced, manhattan
        #default puzzles are the different difficulty of puzzles
        default_puzzles()

    if puzzle_mode == 2:
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

        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        #select_algo(user_puzzle)

    return
    
#this menu needs to be changed 
def select_algo(puzzle):
    algorithm = input("Select algorithm. (1) uniform cost search (2) A* Misplaced Tile Heuristic (3) A* Manhattan Distance Heuristic")
    if algorithm == 1:
        uniform_cost_search(puzzle)
    if algorithm == 2:
        misplaced_tile_search(puzzle)
    if algorithm == 3:
        manhattan_heuristic(puzzle)

def default_puzzles():
    difficulty = input(
        "Please enter a desired difficulty on a scale from 0 to 5. \n")
    if difficulty == 0:
        print("Difficulty of 'Trivial' selected.")
        select_algo(trivial)
    if difficulty == 1:
        print("Difficulty of 'Very Easy' selected.")
        select_algo(veryEasy)
    if difficulty == 2:
        print("Difficulty of 'Easy' selected.")
        select_algo(easy)
    if difficulty == 3:
        print("Difficulty of 'Medium' selected.")
        select_algo(medium)
    if difficulty == 4:
        print("Difficulty of 'Hard' selected.")
        select_algo(hard)
    if difficulty == 5:
        print("Difficulty of 'Impossible' selected.")
        select_algo(impossible)
    

def print_puzzle(puzzle):
    for i in range(0,3):
        print(puzzle[i])
    print('\n')


#default puzzle options
trivial = [[1, 2, 3],
[4, 5, 6],
[7, 8, 0]]
veryEasy = [[1, 2, 3],
[4, 5, 6],
[7, 0, 8]]
easy = [[1, 2, 0],
[4, 5, 3],
[7, 8, 6]]
medium = [[0, 1, 2],
[4, 5, 3],
[7, 8, 6]]
hard = [[8, 7, 1],
[6, 0, 2],
[5, 4, 3]]

#https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
#impossible state cited from ^
impossible = [[8, 1, 2],
[0, 4, 3],
[7, 6, 5]]

#compare this to every state to see if the puzzle is finished 
goalState = [[1, 2, 3], 
             [4, 5, 6], 
             [7, 8, 0]]

# class to define each puzzle state 
class Puzzle:
    def __init__(self, state, parent = None, depth = 0, cost = 0):
        self.state = state
        self.parent = parent 
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


#to move the blank space around the puzzle
#up
#down
#left 
#right
def goal_pos(goalState, state): 
    for i in range(3):
        for j in range (3):
            if goalState[i][j] == state:
                return i, j

def manhattan_heuristic(state):
    #check the current state and see how far the blank is from the goal 
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_column = goal_pos(goalState, state[i][j])
                distance += abs(i - goal_row) + abs(j - goal_column)
    print('Manhatten: ' + str(distance))
    return distance
main()
#def a_star_search(puzzle):
    
#need to evaluate which state is the most promising 
#f = cost + estimated cost 

#def uniform_cost_search(puzzle):