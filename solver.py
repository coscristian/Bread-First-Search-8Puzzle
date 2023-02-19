class Node:
    def __init__(self, board: str):
        # Store the children nodes when moving Left, Up, Right or Down
        self.children = []
        # Store its parent node to track the path to the solution
        self.parent = None
        # Board
        self.board = board
        # Blank space
        self.x = 'e'

        # Number of columns
        self.columns = 3
        # Set the initial board (Can be changed to self.board = initial)
        #self.set_board(initial)

    def set_board(self, new_board: list) -> None:
        #self.board = new_board[::]
        for i in range(len(self.board)):
            self.board[i] = new_board[i]

    def print_board(self) -> None:
        print()
        m = 0
        for i in range(self.columns):
            for j in range(self.columns):
                print(self.board[m], end=" ")
                m += 1
            print()

    def is_same_board(self, b: list) -> bool:
        same_board = True
        for i in range(len(b)):
            if self.board[i] != b[i]:
                same_board = False
        return same_board

    def expand_node(self) -> None:
        blank_index = 0
        for i in range(len(self.board)):
            if self.board[i] == 'e':
                blank_index = i

        self.move_to_right(self.board, blank_index) 
        self.move_to_left(self.board, blank_index)
        self.move_to_up(self.board, blank_index)
        self.move_to_down(self.board, blank_index)

    def move_to_right(self, b:list, i:int): #i: index of the 'e'
        if i % self.columns < self.columns - 1: 
            # Avoid to change my current puzzle 
            self.possible_move = [""] * (self.columns * self.columns)
            self.copy_board(self.possible_move, b)

            # Change positions
            temp = self.possible_move[i + 1]
            self.possible_move[i+1] = self.possible_move[i]
            self.possible_move[i] = temp

            # Create child and assign parent
            child = Node(self.possible_move)
            self.children.append(child)
            child.parent = self
    
    def move_to_left(self, b:list, i:int):
        if i % self.columns > 0:
            self.possible_move = [""] * (self.columns * self.columns)
            self.copy_board(self.possible_move, b)

            temp = self.possible_move[i - 1]
            self.possible_move[i - 1] = self.possible_move[i]
            self.possible_move[i] = temp

            child = Node(self.possible_move)
            self.children.append(child)
            child.parent = self

    def move_to_up(self, b:list, i:int):
        if i - self.columns >= 0:
            self.possible_move = [""] * (self.columns * self.columns)
            self.copy_board(self.possible_move, b)

            temp = self.possible_move[i - 3]
            self.possible_move[i - 3] = self.possible_move[i]
            self.possible_move[i] = temp

            child = Node(self.possible_move)
            self.children.append(child)
            child.parent = self

    def move_to_down(self, b:list, i:int):
        if i + self.columns < len(self.board):
            self.possible_move = [""] * (self.columns * self.columns)
            self.copy_board(self.possible_move, b)

            temp = self.possible_move[i + 3]
            self.possible_move[i + 3] = self.possible_move[i]
            self.possible_move[i] = temp

            child = Node(self.possible_move)
            self.children.append(child)
            child.parent = self

    def copy_board(self, a:list, b:list):
        for i in range(len(b)):
            a[i] = b[i]

    def is_goal(self):
        goal = True
        m = self.board[0]
        for i in range(1, len(self.board)):
            if m > self.board[i]:
                goal = False
            m = self.board[i]
        return goal

class Solver:
    pass


initial = "1 2 4 3 e 5 7 6 8"
initial = initial.split()

hola = []

for i in range(len(initial)):
    hola[i] = initial[i]

print(hola)
#initial_node = Node(initial)
#initial_node.set_board(initial)
