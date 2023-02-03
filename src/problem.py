import copy
from heuristic import misplaced_tiles, total_distance_goal
import heapq
import json

# CONSTANTS
UP = 3
DOWN = 1
RIGHT = 2
LEFT = 0
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


class heapNode:
    def __init__(self , data , value):
        self.data = data
        self.value = value

    def __lt__(self, other):   #To override > operator
        return self.value < other.value

    def __gt__(self , other):  #To override < operator
        return self.value > other.value

    def get(self):
        return self.data
# some functions for all conditions
def is_solved(puzzle: list) -> bool:
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if(puzzle[i][j] != count):
                return False
            count += 1
    return True

def concat_dir(cur: tuple, direction:int) -> tuple:
    return (cur[0] + DIRECTIONS[direction][0], cur[1] + DIRECTIONS[direction][1])

def swap(l1: tuple, l2: tuple, puzzle: list) -> list:
    puzzle_new = copy.deepcopy(puzzle)
    v = puzzle_new[l1[0]][l1[1]]
    puzzle_new[l1[0]][l1[1]] = puzzle_new[l2[0]][l2[1]]
    puzzle_new[l2[0]][l2[1]] = v
    return puzzle_new

def show_format_puzzle(puzzle: list) -> str:
    r = ""
    for i in puzzle:
        r += str(i) + "\n"
    return r[:-1]

# note that the location tuple is (y,x)

class PuzzleSolver:
    move_counts = 0
    puzzle = []
    base_puzzle = []
    open = []
    closed = []
    num_node_created = 0
    num_node_poped = 0
    def __init__(self , puzzle:list) -> None:
        self.puzzle  = puzzle
        self.base_puzzle = puzzle
        self.open = []
        self.num_node_created = 0
    # cost, action, puzzle, parent inside node
    def push(self, node: heapNode):
        heapq.heappush(self.open, node)
        self.num_node_created += 1
    
    def pop(self):
        self.num_node_poped += 1
        node = heapq.heappop(self.open)
        return node.get()
    
    def trace_back(self, node) -> list:
        actions = []
        while node["parent"]:
            actions.append(node["action"])
            node = node["parent"]
        actions.reverse()
        return actions
    
    def is_valid_loc(self, loc:tuple) -> bool:
        if loc[0] < 0 or loc[0] >= len(self.puzzle) or loc[1] < 0 or loc[1] >= len(self.puzzle):
            return False
        return True

    def find_current_0_loc(self , puz = None) -> tuple:
        if not puz:
            puz = self.puzzle
        for i in range(len(puz)):
            for j in range(len(puz[i])):
                if(puz[i][j] == 0):
                    return (i, j)

    def move(self, direction:int, count:bool = True, puz:list = None) -> list: # in algorithm, don't assign count and puz
        if count:
            self.move_counts += 1
        if not puz:
            puz = self.puzzle
        cur = self.find_current_0_loc(puz)
        next_loc = concat_dir(cur, direction)
        if not self.is_valid_loc(next_loc):
            raise Exception(f"illegal move {next_loc} from {cur} in {direction}")
        return swap(cur, next_loc, puz)

    def possible_moves(self, puzzle = None):
        if not puzzle:
            puzzle = self.puzzle
        cur = self.find_current_0_loc(puzzle)
        trys = [UP, DOWN, RIGHT, LEFT]
        re = []
        for i in trys:
            if(self.is_valid_loc(concat_dir(cur, i))):
                re.append(i)
        return re
    def output_visualize(self, solution: list):
        return(json.dumps({"actions": solution , "puzzle": self.base_puzzle}))
    
    def output_performance(self) -> str:
        return f"move counts: {self.move_counts}, node gen: {self.num_node_created}, node pop: {self.num_node_poped}"
    # test function
    def show_text_frame(self, actions: list) -> None:
        new_puzzle = copy.deepcopy(self.base_puzzle)
        print(show_format_puzzle( new_puzzle))
        print("=============================")
        for i in actions:
            new_puzzle = self.move(i,False, new_puzzle)
            print(show_format_puzzle(new_puzzle))
            print("=============================")
        print(f"move counts: {self.move_counts}, node gen: {self.num_node_created}, node pop: {self.num_node_poped}")

    # returns a list of directions
    # some functions 
    def bfs(self) -> list:
        cur_node = {"action" : -1, "puzzle" : self.puzzle, "parent" : None}
        self.open.append(cur_node)
        while self.open:
            self.num_node_poped += 1
            cur_node = self.open.pop(0) #used as a queue
            # print(cur_node)
            if(is_solved(cur_node["puzzle"])):
                # print(cur_node)
                return self.trace_back(cur_node)#[1:]
            self.closed.append(cur_node["puzzle"])
            self.puzzle = cur_node["puzzle"]
            possible_moves = self.possible_moves()
            for i in possible_moves:
                new_puzzle = self.move(i)
                new_node = {"action": i, "puzzle": new_puzzle, "parent": cur_node}
                if(not new_puzzle in self.closed):
                    self.num_node_created += 1
                    self.open.append(new_node)
                
        raise Exception("no solution")
        return []
    
    def iddfs(self , max_depth: int) -> list:
        for i in range(max_depth + 1):
            self.puzzle = copy.deepcopy(self.base_puzzle)
            self.closed = []
            self.open = []
            try:
                to_return = self.dfs(i)
                return to_return
            except:
                continue
        raise Exception("no solution")
    
    def dfs(self, depth = -1) -> list:
        cur_node = {"action" : -1, "puzzle" : self.puzzle, "parent" : None, "depth": 0}
        # print(cur_node , depth)
        self.open.append(cur_node)
        while self.open:
            self.num_node_poped += 1
            cur_node = self.open.pop() #used as a stack
            if(is_solved(cur_node["puzzle"])):
                return self.trace_back(cur_node)
            self.closed.append(cur_node["puzzle"])
            self.puzzle = cur_node["puzzle"]
            # print(depth , cur_node["depth"])
            if cur_node["depth"] != depth: #can be replaced to < != works with depth = -1 (no depth restrictions)
                possible_moves = self.possible_moves()
                for i in possible_moves:
                    new_puzzle = self.move(i)
                    new_node = {"action": i, "puzzle": new_puzzle, "parent": cur_node, "depth": cur_node["depth"] + 1}
                    if(not new_puzzle in self.closed):
                        self.num_node_created += 1
                        self.open.append(new_node)
        raise Exception("no solution")
    
    def a_star(self, depth = -1, func = misplaced_tiles) -> list:
        cur_node =  heapNode({ "depth":0, "action" : -1, "puzzle" : self.puzzle, "parent" : None}, 0)
        # print(cur_node , depth)
        self.push(cur_node)
        while self.open:
            cur_node = self.pop() #used heap
            if(is_solved(cur_node["puzzle"])):
                return self.trace_back(cur_node)
            self.closed.append(cur_node["puzzle"])
            self.puzzle = cur_node["puzzle"]
            # print(depth , cur_node["depth"])
            if cur_node["depth"] != depth: #can be replaced to < != works with depth = -1 (no depth restrictions)
                possible_moves = self.possible_moves()
                for i in possible_moves:
                    new_puzzle = self.move(i)
                    if(not new_puzzle in self.closed):
                        f_val = cur_node["depth"] + 1 + func(new_puzzle)
                        new_node =  heapNode({ "action": i, "puzzle": new_puzzle, "parent": cur_node, "depth": cur_node["depth"] + 1}, f_val)
                        self.push(new_node)
        raise Exception("no solution")

    def ida_star(self , max_depth: int , func = misplaced_tiles ) -> list:
        for i in range(max_depth + 1):
            self.puzzle = copy.deepcopy(self.base_puzzle)
            self.closed = []
            self.open = []
            try:
                to_return = self.a_star(i,func)
                return to_return
            except:
                continue
        raise Exception("no solution")
