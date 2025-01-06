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
        self.markedVisited = []
        self.horizontal_matrix = horizontal_matrix
        self.vertical_matrix = vertical_matrix
        self.gruben = gruben
        self.width = width
        self.height = height
        self.cost_matrix = []

    def get_neighbors(self, x, y):
        neighbors = []
        if test_right(x, y, self.vertical_matrix) and (x + 1, y) not in self.markedVisited:
            neighbors.append((x + 1, y, 1))
        if test_left(x, y, self.vertical_matrix) and (x - 1, y) not in self.markedVisited:
            neighbors.append((x - 1, y, 0))
        if test_up(x, y, self.horizontal_matrix) and (x, y - 1) not in self.markedVisited:
            neighbors.append((x, y - 1, 3))
        if test_down(x, y, self.horizontal_matrix) and (x, y + 1) not in self.markedVisited:
            neighbors.append((x, y + 1, 2))

        # index 2 is the direction the neighbors has to go to reach the current node
        return neighbors

    def write_cost(self, x, y):
        has_to_visit = self.get_neighbors(x, y)
        self.cost_matrix[y][x] = 4
        a = 0
        while has_to_visit:
            if a == 1000:
                print(len(has_to_visit))
                a = 0
            a += 1
            current = has_to_visit.pop(0)
            self.cost_matrix[current[1]][current[0]] = current[2]
            for j in self.get_neighbors(current[0], current[1]):
                if self.cost_matrix[j[1]][j[0]] is None:
                    has_to_visit.append(j)


    def create_cost_matrix(self):
        self.cost_matrix = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.write_cost(self.width - 1, self.height - 1)
        return self.cost_matrix


class solving:

    def __init__(self, cost_matrix_1, cost_matrix_2, vertical_matrix_1, horizontal_matrix_1, vertical_matrix_2,
                 horizontal_matrix_2, width, height):
        self.cost_matrix_1 = cost_matrix_1
        self.cost_matrix_2 = cost_matrix_2
        self.width = width
        self.height = height
        self.horizontal_matrix_1 = horizontal_matrix_1
        self.vertical_matrix_1 = vertical_matrix_1
        self.horizontal_matrix_2 = horizontal_matrix_2
        self.vertical_matrix_2 = vertical_matrix_2
        self.visited = []

    def neighbours_cost(self, moves):
        e, f = self.next_move(moves, self.vertical_matrix_1, self.horizontal_matrix_1, self.cost_matrix_1), \
            self.next_move(moves, self.vertical_matrix_2, self.horizontal_matrix_2, self.cost_matrix_2)

        if e == 4 or f == 4:
            return [(moves + [e if e != 4 else f], self.get_total_cost(moves + [e if e != 4 else f]))]

        new_moves_e, new_moves_f = moves + [e], moves + [f]
        h, g = (new_moves_e, self.get_total_cost(new_moves_e)), (new_moves_f, self.get_total_cost(new_moves_f))

        h = self.update_visited(h, new_moves_e)
        g = self.update_visited(g, new_moves_f)

        return [h, g] if e != f else [h]

    def next_move(self, movements, vertical_matrix, horizontal_matrix, cost_matrix):
        at_the_moment = self.calculate_position(movements, vertical_matrix, horizontal_matrix)
        return 4 if at_the_moment == (self.width - 1, self.height - 1) else \
            cost_matrix[at_the_moment[1]][at_the_moment[0]]

    def get_total_cost(self, movements):
        return self.get_moving_cost(movements, self.vertical_matrix_1, self.horizontal_matrix_1, self.cost_matrix_1) + \
            self.get_moving_cost(movements, self.vertical_matrix_2, self.horizontal_matrix_2, self.cost_matrix_2)

    def get_moving_cost(self, movements, vertical_matrix, horizontal_matrix, cost_matrix):
        at_the_moment = self.calculate_position(movements, vertical_matrix, horizontal_matrix)
        if at_the_moment == (self.width - 1, self.height - 1):
            return 0  # Ziel erreicht
        return cost_matrix[at_the_moment[1]][at_the_moment[0]]

    def calculate_position(self, movements, vertical_matrix, horizontal_matrix):
        at_the_moment = (0, 0)
        move_funcs = [test_right, test_left, test_up, test_down]
        move_deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for move in movements:
            if at_the_moment == (self.width - 1, self.height - 1):
                break
            if move_funcs[move](at_the_moment[0], at_the_moment[1], vertical_matrix if move < 2 else horizontal_matrix):
                at_the_moment = (at_the_moment[0] + move_deltas[move][0], at_the_moment[1] + move_deltas[move][1])

        return at_the_moment

    def update_visited(self, move_cost_tuple, new_moves):
        pos = (self.calculate_position(new_moves, self.vertical_matrix_1, self.horizontal_matrix_1),
               self.calculate_position(new_moves, self.vertical_matrix_2, self.horizontal_matrix_2))
        if pos in self.visited:
            return None
        else:
            self.visited.append(pos)
        return move_cost_tuple
