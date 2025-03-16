from cost import test_right, test_left, test_up, test_down

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
        self.visited = {}

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

    def next_move(self, at_the_moment, cost_matrix):
        return None if at_the_moment == (self.width - 1, self.height - 1) else \
            cost_matrix[at_the_moment[1]][at_the_moment[0]][1]

    def get_total_cost(self, at_the_moment):
        return self.get_moving_cost(at_the_moment[0], self.cost_matrix_1) + \
            self.get_moving_cost(at_the_moment[1], self.cost_matrix_2)

    def get_moving_cost(self, at_the_moment, cost_matrix):
        if at_the_moment == (self.width - 1, self.height - 1):
            return 0  # Ziel erreicht
        return cost_matrix[at_the_moment[1]][at_the_moment[0]][0]

    def check_visited(self, current_position, next_position, length, e):
        pos = position(next_position[0], next_position[1], length, current_position)
        if pos in self.visited:
            return None
        self.visited[pos] = length
        return e

    def neighbours_cost(self, moves):
        current_position = (self.calculate_position(moves, self.vertical_matrix_1, self.horizontal_matrix_1),
                            self.calculate_position(moves, self.vertical_matrix_2, self.horizontal_matrix_2))
        e, f = self.next_move(current_position[0], self.cost_matrix_1), \
            self.next_move(current_position[1], self.cost_matrix_2)

        next_postion_e = self.next_postion(current_position, e) if e is not None else None
        next_postion_f = self.next_postion(current_position, f) if f is not None else None

        e = self.check_visited(current_position, next_postion_e, len(moves) + 1, e) if e is not None else None
        f = self.check_visited(current_position, next_postion_f, len(moves) + 1, f) if f is not None else None

        h = (moves + [e], self.get_total_cost(next_postion_e)) if e is not None else None
        g = (moves + [f], self.get_total_cost(next_postion_f)) if f is not None else None

        return [h, g] if h is not None and g is not None else [h] if h is not None else [g] if g is not None else []


class position:
    def __init__(self, position_1, position_2, length, vorgaenger):
        self.x = position_1[0]
        self.y = position_1[1]
        self.z = position_2[0]
        self.w = position_2[1]
        self.length = length
        self.vorgaenger = vorgaenger

    def __eq__(self, other):
        if not isinstance(other, position):
            return NotImplemented
        return (self.x, self.y, self.z, self.w) == (other.x, other.y, other.z, other.w)

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.w))

