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
        current_position = (self.calculate_position(moves, self.vertical_matrix_1, self.horizontal_matrix_1),
                            self.calculate_position(moves, self.vertical_matrix_2, self.horizontal_matrix_2))
        e, f = self.next_move(current_position[0], self.cost_matrix_1), \
            self.next_move(current_position[1], self.cost_matrix_2)

        if e == 4 or f == 4:
            if e == 4:
                current_position = (self.calculate_position(moves+[f], self.vertical_matrix_1, self.horizontal_matrix_1),
                                    self.calculate_position(moves+[f], self.vertical_matrix_2, self.horizontal_matrix_2))
                return [(moves + [f], self.get_total_cost(current_position))]
            current_position = (self.calculate_position(moves + [e], self.vertical_matrix_1, self.horizontal_matrix_1),
                                self.calculate_position(moves + [e], self.vertical_matrix_2, self.horizontal_matrix_2))
            return [(moves + [e], self.get_total_cost(current_position))]

        next_postion_e = self.next_postion(current_position, e)
        next_postion_f = self.next_postion(current_position, f)

        new_moves_e, new_moves_f = moves + [e], moves + [f]
        h, g = (new_moves_e, self.get_total_cost(next_postion_e)), (new_moves_f, self.get_total_cost(next_postion_f))

        h = self.update_visited(next_postion_e, h)
        g = self.update_visited(next_postion_f, g)

        return [h, g] if e != f else [h]

    def next_move(self, at_the_moment, cost_matrix):
        return 4 if at_the_moment == (self.width - 1, self.height - 1) else \
            cost_matrix[at_the_moment[1]][at_the_moment[0]][1]

    def get_total_cost(self, at_the_moment):
        return self.get_moving_cost(at_the_moment[0], self.cost_matrix_1) + \
            self.get_moving_cost(at_the_moment[1], self.cost_matrix_2)

    def next_postion(self, at_the_moment, next_move):
        move_funcs = [test_right, test_left, test_up, test_down]
        move_deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        pos_x, pos_y = at_the_moment[0], at_the_moment[1]
        if move_funcs[next_move](at_the_moment[0][0], at_the_moment[0][1],
                                 self.vertical_matrix_1 if next_move < 2 else self.horizontal_matrix_1):
            pos_x = (at_the_moment[0][0] + move_deltas[next_move][0], at_the_moment[0][1] + move_deltas[next_move][1])
        if move_funcs[next_move](at_the_moment[1][0], at_the_moment[1][1],
                                 self.vertical_matrix_2 if next_move < 2 else self.horizontal_matrix_2):
            pos_y = (at_the_moment[1][0] + move_deltas[next_move][0], at_the_moment[1][1] + move_deltas[next_move][1])
        return pos_x, pos_y

    def get_moving_cost(self, at_the_moment, cost_matrix):
        if at_the_moment == (self.width - 1, self.height - 1):
            return 0  # Ziel erreicht
        return cost_matrix[at_the_moment[1]][at_the_moment[0]][0]

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

    def update_visited(self, pos, move_cost_tuple):
        if pos in self.visited:
            return None
        else:
            self.visited.append(pos)
        return move_cost_tuple
