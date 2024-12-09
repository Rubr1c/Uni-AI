import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# required packages 
required_packages = ["matplotlib", "numpy"]

# install packages if not present
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
    """
    A class for creating and solving mazes with visual representation.
    
    This class provides methods for:
    1. Visualizing the maze using matplotlib
    2. Setting start and end points
    3. Solving the maze using BFS or A* algorithms
    4. Displaying the search process and final path
    
    Attributes:
        maze (np.array): 2D array representing the maze
        window (plt.Figure): Matplotlib figure for visualization
        graph (plt.Axes): Matplotlib axes for the maze plot
        image (plt.AxesImage): Image representation of the maze
        start (tuple): Starting position (row, col)
        end (tuple): Goal position (row, col)
        annotations (dict): Dictionary storing cell annotations for A* values
    """
    def __init__(self, matrix):
        """
        Initialize the maze with a given matrix.
        
        Parameters:
            matrix (list): 2D list representing the initial maze configuration
                         0 = empty cell, 1 = wall
        """
        self.maze = np.array(matrix)
        
        # map colors
        cmap = colors.ListedColormap(['black', 'white', 'red', 'green', 'yellow'])
        
        self.window, self.graph = plt.subplots()
        self.image = self.graph.imshow(self.maze, cmap=cmap, 
                                     norm=colors.BoundaryNorm([0, 1, 2, 3, 4, 5], cmap.N), 
                                     interpolation='none')
        # interactive mode
        plt.ion()  

        self.graph.axis('off')
        self.annotations = {}

    def set_start(self, start_pos):
        """
        Set the starting position in the maze.
        
        Parameters:
            start_pos (tuple): Starting position as (row, col)
        """
        self.start = start_pos
        self.update_square(start_pos[0], start_pos[1], 3)

    def set_end(self, end_pos):
        """
        Set the goal position in the maze.
        
        Parameters:
            end_pos (tuple): Goal position as (row, col)
        """
        self.end = end_pos
        self.update_square(end_pos[0], end_pos[1], 3)

    def update_square(self, row, col, value):
        """
        Update a maze cell color and refresh the display.
        
        Parameters:
            row (int): Row index of the cell
            col (int): Column index of the cell
            value (int): Color value for the cell (0-4)
        """
        self.maze[row, col] = value
        self.image.set_data(self.maze)
        plt.draw()
        plt.pause(0.1)

    def show_maze(self):
        """
        Refresh the maze display.
        """
        self.image.set_data(self.maze)
        plt.draw()
        plt.pause(0.1)

    def trace_path(self, path):
        """
        gets best path from solution of the maze.
        
        Parameters:
            path (list): (row, col)[] positions forming the path
        """
        for row, col in path:
            self.update_square(row, col, 4)  # Mark path in yellow
        time.sleep(1)

    def bfs(self):
        """
        Solve the maze using BFS.
        
        Returns:
            list: (row, col)[] positions of the shortest path or empty list if no path is found
        """
        queue = [self.start]  # queue with start position
        visited = set()       # visited cells
        parent = {self.start: None}  # Store parent cells for each pos to find shorest path later
        
        # right, down, left, up
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Main BFS loop: Process cells in queue
        while queue:
            time.sleep(0.5)
            current = queue.pop(0)  # next cell to explore
            visited.add(current)    # set current cell as visited
            self.update_square(current[0], current[1], 2)
            
            # Check if we reached the goal
            if current == self.end:
                # Trace back from goal to start
                path = []
                while current:  # Loop until we reach start
                    path.append(current)
                    current = parent[current]
                path.reverse()  # Reverse to get path from start to goal
                self.trace_path(path)
                return path

            # check all possible moves
            for move in moves:
                neighbor = (current[0] + move[0], current[1] + move[1])
                # Check if neighbor is valid and unvisited:
                if (0 <= neighbor[0] < self.maze.shape[0] and
                    0 <= neighbor[1] < self.maze.shape[1] and
                    (self.maze[neighbor] == 0 or self.maze[neighbor] == 3) and
                    neighbor not in visited):
                    queue.append(neighbor)     # add to queue for later exploration
                    visited.add(neighbor)      # set as visited to avoid re-queuing
                    parent[neighbor] = current # store parent for path
        return []  # empty list if no path found

    def a_star(self):
        """
        Solve the maze using A* Search algorithm and calculate the total cost.
        Returns:
            tuple: (path, total_cost)
                path: (row, col)[] positions forming the optimal path.
                total_cost: The total cost of the path.
        """
        p_queue = PriorityQueue()  # priority queue for A* frontier
        visited = set()            # visited cells
        parent = {self.start: None}  # Store parent cells for each pos to find shorest path later
        g_score = {self.start: 0}  # cost from start to each node

        # Initialize with start position:
        # (heuristic, cost, position, path)
        p_queue.put((self.heuristic(self.start), 0, self.start, [self.start]))
        visited.add(self.start)

        # Main A* loop: Process cells by lowest heuristic
        while not p_queue.empty():
            time.sleep(0.5)  
            # Get next cell with lowest heuristic
            f_value, current_cost, vertex, path = p_queue.get()
            self.update_square(vertex[0], vertex[1], 2)  # set as visited

            # Check if goal reached
            if vertex == self.end:
                self.trace_path(path)
                return path, current_cost

            # right, down, left, up
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            # check each possible move
            for dr, dc in moves:
                neighbor = (vertex[0] + dr, vertex[1] + dc)
                if (0 <= neighbor[0] < self.maze.shape[0] and
                    0 <= neighbor[1] < self.maze.shape[1] and
                    (self.maze[neighbor] == 0 or self.maze[neighbor] == 3) and
                    neighbor not in visited):

                    tentative_g_score = current_cost + 1  # cost from start
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        g_score[neighbor] = tentative_g_score
                        parent[neighbor] = vertex
                        h_value = self.heuristic(neighbor)  # heuristic of neighbor 
                        f_value = tentative_g_score + h_value  # cost + heuristic
                        
                        # show cost and heuristic in cell
                        self.add_number(neighbor[0], neighbor[1], f"{h_value} | {f_value}")
                        p_queue.put((f_value, tentative_g_score, neighbor, path + [neighbor]))

        return [], float('inf')  # empty path and infinite cost if no path found


    def add_number(self, row, col, number):
        """
        Add or update a text annotation in a maze cell.
        
        Args:
            row (int): Row index of the cell
            col (int): Column index of the cell
            number (str): Text to display in the cell
        """
        if (row, col) in self.annotations:
            self.annotations[(row, col)].remove()
        self.annotations[(row, col)] = self.graph.text(
            col, row, number, ha='center', va='center', color='blue', fontsize=10
        )
        plt.draw()
        plt.pause(0.1)

    def heuristic(self, pos):
        """
        Calculate the Manhattan distance heuristic.
        
        Args:
            pos (tuple): Current position as (row, col)
            
        Returns:
            int: Manhattan distance to the goal
        """
        return abs(self.end[0] - pos[0]) + abs(self.end[1] - pos[1])


if __name__ == "__main__":
    # Create a sample maze
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
    
    maze_bfs = Maze(matrix)
    maze_bfs.set_start((0, 0))
    maze_bfs.set_end((9, 9))
    print("BFS Path:", maze_bfs.bfs())
    plt.title("BFS Search")
    plt.show()

    maze_astar = Maze(matrix)
    maze_astar.set_start((0, 0))
    maze_astar.set_end((9, 9))
    path, total_cost = maze_astar.a_star()  
    print("A* Path:", path)
    print("A* Total Cost:", total_cost)
    maze_astar.graph.set_title(f"A* Search\nTotal Cost: {total_cost}")
    plt.pause(3)
    plt.close()
    