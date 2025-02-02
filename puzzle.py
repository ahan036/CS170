import heapq 
#hello did this work
def main():
    puzzle_mode = input("Welcome to Ashley's puzzle solver. Type '1' to use a default puzzle, or '2' to create your own \n")

    if puzzle_mode == "1":
        #select algo chooses between: uniform, misplaced, manhattan
        #default puzzles are the different difficulty of puzzles
        select_algo(default_puzzles())

    if puzzle_mode == "2":
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
        select_algo(user_puzzle)

    return
    
def select_algo():
    algorithm = input("Select algorithm. (1) uniform cost search (2) A* Misplaced Tile Heuristic (3) A* Manhattan Distance Heuristic")
    if algorithm == "1":
        uniform_cost_search(puzzle, 0)
    if algorithm == "2":
        misplaced_tile_search(puzzle, 1)
    if algorithm == "3":
        manhattan_search(puzzle, 2)

def default_puzzle():
    difficulty = input(
        "Please enter a desired difficulty on a scale from 0 to 5. \n")
    if difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    if difficulty == "2":
        print("Difficulty of 'Easy' selected.")
        return easy
    if difficulty == "3":
        print("Difficulty of 'Medium' selected.")
        return medium
    if difficulty == "4":
        print("Difficulty of 'Hard' selected.")
        return hard
    if difficulty == "5":
        print("Difficulty of 'Impossible' selected.")
        return impossible
    

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
class Node:
    def __init__(self, state):
        self.state = state