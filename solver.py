import graphviz

class Node:
    def __init__(self, board: list):
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
            if self.board[i] == '0':
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
        m = self.board[0]
        for i in range(1, len(self.board)):            
            if int(m) > int(self.board[i]):
                return False
            m = self.board[i]
        return True
        
class Solver:
    def __init__(self) -> None:
        pass

    def get_amount_movements(self):
        return self.__amount_movements
    def get_amount_enqueue_nodes(self):
        return self.__amount_enqueue

    # Returns list of nodes which is the path
    def breadth_first_search(self, root:Node) -> list:

        def path_trace(path: list, n: Node) -> int:
            current : Node = n
            path.append(current)
            movements = 0
            
            while current.parent != None:
                movements += 1
                current = current.parent
                path.append(current)
            return movements

        def contains(nodes: list, c: Node) -> bool:
            contains = False
            for i in range(len(nodes)):
                n : Node = nodes[i]
                if n.is_same_board(c.board):
                    contains = True
            return contains

        path_to_solution = []
        #Keeps the nodes that can be expanded
        open_list = []
        # Store the nodes that have been already expanded
        closed_list = []

        open_list.append(root)
        self.__amount_enqueue = 1
        goal_found = False
        
        while len(open_list) > 0 and not goal_found:
            # Implementing queue
            current_node : Node = open_list[0]
            closed_list.append(current_node)
            
            open_list.pop(0)

            current_node.expand_node()
            
            for i in range(len(current_node.children)):
                current_child : Node = current_node.children[i]
                if current_child.is_goal():
                    goal_found = True
                    self.__amount_movements = path_trace(path_to_solution, current_child)

                if not contains(open_list, current_child) and not contains(closed_list, current_child):
                    open_list.append(current_child)
                    self.__amount_enqueue += 1
        return path_to_solution


g = graphviz.Digraph('G', filename='hello.gv')

g.node('A', '1 2 4\n3 0 5\n7 6 8')
g.node('B', 'Hello All')
g.node('C', 'H')

g.edges(['AB', 'AC'])
g.view()

initial = "1 2 4 3 0 5 7 6 8"

initial = initial.split()
root_node = Node(initial)

solve = Solver()
solution : list = solve.breadth_first_search(root_node)
solution.reverse()
if len(solution) > 0:
    print("Goal Found !!!!! \n Tracing path...")
    print(f"Amount of movements: {solve.get_amount_movements()}")
    print(f"Amount of enqueue nodes: {solve.get_amount_enqueue_nodes()}")
    board : Node
    for board in solution:
        board.print_board()
else:
    print("No path to solution is found !!!")