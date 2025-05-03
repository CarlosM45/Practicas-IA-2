import heapq

class OnlineAStar:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = (0, 0)
        self.goal = (self.rows - 1, self.cols - 1)
        self.open_set = []
        self.closed_set = set()
        self.g_scores = {self.start: 0}
        self.parent = {}

    def heuristic(self, cell):
        # Distancia Manhattan
        return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])

    def get_neighbors(self, cell):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in directions:
            new_row, new_col = cell[0] + d[0], cell[1] + d[1]
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.maze[new_row][new_col] == 0:
                neighbors.append((new_row, new_col))
        return neighbors

    def reconstruct_path(self):
        path = []
        current = self.goal
        while current in self.parent:
            path.append(current)
            current = self.parent[current]
        path.append(self.start)
        return path[::-1]

    def search(self):
        heapq.heappush(self.open_set, (self.heuristic(self.start), self.start))

        while self.open_set:
            _, current = heapq.heappop(self.open_set)

            if current == self.goal:
                return self.reconstruct_path()

            self.closed_set.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in self.closed_set:
                    continue

                tentative_g_score = self.g_scores[current] + 1

                if neighbor not in self.g_scores or tentative_g_score < self.g_scores[neighbor]:
                    self.g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor)
                    heapq.heappush(self.open_set, (f_score, neighbor))
                    self.parent[neighbor] = current

        return None  # No se encontró un camino

# Ejemplo de uso
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

solver = OnlineAStar(maze)
path = solver.search()

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró un camino.")