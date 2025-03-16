def test_right(x, y, vertical_matrix):
    if x < len(vertical_matrix[0]):
        if vertical_matrix[y][x] == 0:
            return True
    return False


def test_left(x, y, vertical_matrix):
    if x > 0:
        if vertical_matrix[y][x - 1] == 0:
            return True
    return False


def test_up(x, y, horizontal_matrix):
    if y > 0:
        if horizontal_matrix[y - 1][x] == 0:
            return True
    return False


def test_down(x, y, horizontal_matrix):
    if y < len(horizontal_matrix):
        if horizontal_matrix[y][x] == 0:
            return True
    return False


class cost:

    def __init__(self, horizontal_matrix, vertical_matrix, gruben, width, height):
        self.stack_solving = []
        self.horizontal_matrix = horizontal_matrix
        self.vertical_matrix = vertical_matrix
        self.gruben = gruben
        self.width = width
        self.height = height
        self.cost_matrix = []

    def get_neighbors(self, x, y):
        neighbors = []
        if test_right(x, y, self.vertical_matrix):
            neighbors.append((x + 1, y, 1))
        if test_left(x, y, self.vertical_matrix):
            neighbors.append((x - 1, y, 0))
        if test_up(x, y, self.horizontal_matrix):
            neighbors.append((x, y - 1, 3))
        if test_down(x, y, self.horizontal_matrix):
            neighbors.append((x, y + 1, 2))

        # index 2 is the direction the neighbor has to go to reach the current node
        return neighbors

    def write_cost(self, start_x, start_y, initial_cost, initial_direction):
        # Stack für iterative Verarbeitung
        stack = [(start_x, start_y, initial_cost, initial_direction)]

        while stack:
            x, y, cost, direction = stack.pop()

            # Überspringe, wenn der Knoten bereits verarbeitet wurde
            if self.cost_matrix[y][x] != 0:
                continue

            # Aktuelle Kosten und Richtung setzen
            self.cost_matrix[y][x] = (cost, direction)

            # Nachbarn hinzufügen
            for neighbor in self.get_neighbors(x, y):
                nx, ny, ndirection = neighbor
                if self.cost_matrix[ny][nx] == 0:  # Nur unbesuchte Nachbarn hinzufügen
                    stack.append((nx, ny, cost + 1, ndirection))

    def create_cost_matrix(self):
        self.cost_matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.write_cost(self.width - 1, self.height - 1, 0, None)
        return self.cost_matrix
