def test_right(x, y, vertical_walls):
    if x < len(vertical_walls[0]):
        if vertical_walls[y][x] == 0:
            return True
    return False


def test_left(x, y, vertical_walls):
    if x > 0:
        if vertical_walls[y][x - 1] == 0:
            return True
    return False


def test_up(x, y, horizontal_walls):
    if y > 0:
        if horizontal_walls[y - 1][x] == 0:
            return True
    return False


def test_down(x, y, horizontal_walls):
    if y < len(horizontal_walls):
        if horizontal_walls[y][x] == 0:
            return True
    return False


class Cost:

    def __init__(self, horizontal_matrix, vertical_matrix, gruben, width, height):
        self.horizontal_walls = horizontal_matrix
        self.vertical_walls = vertical_matrix
        self.gruben = gruben
        self.width = width
        self.height = height
        self.matrix = []

    def get_neighbors(self, x, y):
        neighbors = []
        if test_right(x, y, self.vertical_walls) and (x, y) not in self.gruben:
            neighbors.append((x + 1, y, 1))
        if test_left(x, y, self.vertical_walls) and (x, y) not in self.gruben:
            neighbors.append((x - 1, y, 0))
        if test_up(x, y, self.horizontal_walls) and (x, y) not in self.gruben:
            neighbors.append((x, y - 1, 3))
        if test_down(x, y, self.horizontal_walls) and (x, y) not in self.gruben:
            neighbors.append((x, y + 1, 2))

        return neighbors

    def write_cost(self, start_x, start_y):
        stack = [(start_x, start_y, 0, None)]

        while stack:
            x, y, cost, direction = stack.pop()
            if self.matrix[y][x] != 0:
                continue

            self.matrix[y][x] = (cost, direction)


            a = self.get_neighbors(x, y)
            for neighbor in a:
                nx, ny, ndirection = neighbor
                if self.matrix[ny][nx] == 0:
                    stack.append((nx, ny, cost + 1, ndirection))


    def create_cost_matrix(self):
        self.matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.write_cost(self.width - 1, self.height - 1)
        return self.matrix
