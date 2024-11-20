import time
import heapq
import tkinter as tk
import sys
import subprocess
import random

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_and_import("tkinter")

class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return (self.cost + self.depth) < (other.cost + other.depth)

    def get_moves(self):
        moves = []
        zero = self.state.index(0)
        if zero % 3 > 0:  
            moves.append((zero - 1, "Left"))
        if zero % 3 < 2:  
            moves.append((zero + 1, "Right"))
        if zero // 3 > 0: 
            moves.append((zero - 3, "Up"))
        if zero // 3 < 2: 
            moves.append((zero + 3, "Down"))
        return moves

    def apply_move(self, pos):
        new_state = list(self.state)
        zero = self.state.index(0)
        new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
        return new_state

    def is_goal(self):
        return self.state == list(range(1, 9)) + [0]

def manhattan(state):
    dist = 0
    for i in range(1, 9):
        dist += abs((state.index(i) // 3) - ((i - 1) // 3)) + abs((state.index(i) % 3) - ((i - 1) % 3))
    return dist

def misplaced_tiles(state):
    return sum([1 if state[i] != 0 and state[i] != i + 1 else 0 for i in range(9)])

def linear_conflict(state):
    conflict = manhattan(state)
    for i in range(3):
        row, col = state[i * 3:(i + 1) * 3], state[i::3]
        conflict += sum(1 for j in range(2) for k in range(j + 1, 3) if row[j] > row[k] > 0)
        conflict += sum(1 for j in range(2) for k in range(j + 1, 3) if col[j] > col[k] > 0)
    return conflict

def is_solvable(state):
    inv_count = sum(
        1
        for i in range(8)
        for j in range(i + 1, 9)
        if state[i] > state[j] > 0
    )
    return inv_count % 2 == 0

def a_star(start, heuristic):
    if not is_solvable(start):
        return None
    visited = set()
    queue = []
    root = Puzzle(start, cost=heuristic(start))
    heapq.heappush(queue, root)
    while queue:
        node = heapq.heappop(queue)
        if node.is_goal():
            path = []
            while node:
                path.append(node)
                node = node.parent
            return path[::-1]
        if tuple(node.state) in visited:
            continue
        visited.add(tuple(node.state))
        for pos, move in node.get_moves():
            new_state = node.apply_move(pos)
            new_cost = node.depth + heuristic(new_state)
            child = Puzzle(new_state, node, move, node.depth + 1, new_cost)
            heapq.heappush(queue, child)
    return None

class PuzzleGUI:
    def __init__(self, root, row, col, initial_state, heuristic, heuristic_name):
        self.frame = tk.Frame(root, borderwidth=2, relief="solid")
        self.frame.grid(row=row, column=col, padx=5, pady=5)
        self.heuristic = heuristic
        self.heuristic_name = heuristic_name
        self.cells = [[None] * 3 for _ in range(3)]
        self.create_grid()
        self.initial_state = initial_state
        self.solve_and_display()

    def create_grid(self):
        for i in range(3):
            for j in range(3):
                self.cells[i][j] = tk.Label(self.frame, text="", width=4, height=2, font=("Helvetica", 16))
                self.cells[i][j].grid(row=i, column=j, padx=2, pady=2)

        tk.Label(self.frame, text=f"Heuristic: {self.heuristic_name}", font=("Helvetica", 10)).grid(row=3, column=0, columnspan=3)

    def update_grid(self, state):
        for i, val in enumerate(state):
            row, col = divmod(i, 3)
            self.cells[row][col].config(text=str(val) if val != 0 else "")

    def solve_and_display(self):
        self.update_grid(self.initial_state)
        path = a_star(self.initial_state, self.heuristic)
        if path is None:
            for row in self.cells:
                for cell in row:
                    cell.config(text="X")
            tk.Label(self.frame, text="Unsolvable", font=("Helvetica", 10), fg="red").grid(row=4, column=0, columnspan=3)
        else:
            for step in path:
                self.update_grid(step.state)
                self.frame.update()
                time.sleep(1)  


def generate_initial_states(count):
    states = []
    while len(states) < count:
        state = list(range(9))
        random.shuffle(state)
        if is_solvable(state) and state != list(range(1, 9)) + [0]:  
            states.append(state)
    return states

if __name__ == "__main__":
    initial_states = generate_initial_states(5) 
    heuristics = [manhattan, misplaced_tiles, linear_conflict]
    heuristic_names = ["Manhattan", "Misplaced Tiles", "Linear Conflict"]

    root = tk.Tk()
    root.title("8-Puzzle Solver")
    row, col = 0, 0

    for state in initial_states:
        for heuristic, name in zip(heuristics, heuristic_names):
            PuzzleGUI(root, row, col, state, heuristic, name)
            col += 1
            if col == 3: 
                col = 0
                row += 1

    root.mainloop()
