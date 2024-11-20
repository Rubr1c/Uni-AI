import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ["matplotlib", "numpy"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        install(package)

import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib import colors
from queue import PriorityQueue

class Maze:
    def __init__(self, matrix):
        self.maze = np.array(matrix)
        cmap = colors.ListedColormap(['black', 'white', 'red', 'green', 'yellow'])
        
        self.window, self.graph = plt.subplots()
        self.image = self.graph.imshow(self.maze, cmap=cmap, 
                                       norm=colors.BoundaryNorm([0, 1, 2, 3, 4, 5], cmap.N), 
                                       interpolation='none')
        plt.ion()

        self.graph.axis('off')
        self.annotations = {}

    def set_start(self, start_pos):
        self.start = start_pos
        self.update_square(start_pos[0], start_pos[1], 3)

    def set_end(self, end_pos):
        self.end = end_pos
        self.update_square(end_pos[0], end_pos[1], 3)

    def set_maze(self, matrix):
        self.maze = np.array(matrix)

    def update_square(self, row, col, value):
        self.maze[row, col] = value
        self.image.set_data(self.maze)

        plt.draw()
        plt.pause(0.1)

    def show_maze(self):
        self.image.set_data(self.maze)
        plt.draw()
        plt.pause(0.1)

    def trace_path(self, path):
        for row, col in path:
            self.update_square(row, col, 4)  
        time.sleep(1)

    def bfs(self):
        queue = [self.start]
        visited = set()
        parent = {self.start: None}

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            time.sleep(0.5)
            current = queue.pop(0)
            visited.add(current)
            self.update_square(current[0], current[1], 2)  
            
            if current == self.end:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                self.trace_path(path)
                return path

            for move in moves:
                neighbor = (current[0] + move[0], current[1] + move[1])
                if (0 <= neighbor[0] < self.maze.shape[0] and
                    0 <= neighbor[1] < self.maze.shape[1] and
                    (self.maze[neighbor] == 0 or self.maze[neighbor] == 3) and
                    neighbor not in visited):
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
        return []

    def a_star(self):
        p_queue = PriorityQueue()
        visited = set()

        p_queue.put((self.heuristic(self.start), 0, self.start, [self.start]))
        visited.add(self.start)

        while p_queue:
            time.sleep(0.5)
            heuristic, cost, vertex, path = p_queue.get()
            self.update_square(vertex[0], vertex[1], 2)

            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            if vertex == self.end:
                self.trace_path(path)
                return path
            for move in moves:
                neighbor = (vertex[0] + move[0], vertex[1] + move[1])
                if (0 <= neighbor[0] < self.maze.shape[0] and
                    0 <= neighbor[1] < self.maze.shape[1] and
                    (self.maze[neighbor] == 0 or self.maze[neighbor] == 3) and
                    neighbor not in visited):
                    
                    visited.add(neighbor)
                    current_cost = cost + 1
                    heuristic = current_cost + self.heuristic(neighbor)
                    self.add_number(neighbor[0], neighbor[1], str(self.heuristic(neighbor)) + " | " + str(heuristic))
                    p_queue.put((heuristic, current_cost, neighbor, path + [neighbor]))
        return []

    def add_number(self, row, col, number):
        if (row, col) in self.annotations:
            self.annotations[(row, col)].remove()
        self.annotations[(row, col)] = self.graph.text(
            col, row, number, ha='center', va='center', color='blue', fontsize=10
        )
        plt.draw()
        plt.pause(0.1)

    def heuristic(self, pos):
        return abs(self.end[0] - pos[0]) + abs(self.end[1] - pos[1])


if __name__ == "__main__":
    matrix = [[0, 1, 1, 1, 1, 0, 1, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
              [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
              [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    maze = Maze(matrix)

    maze.set_start((0, 0))
    maze.set_end((9, 9))

    # print("BFS Path:", maze.bfs())
    print("A* Path:", maze.a_star())