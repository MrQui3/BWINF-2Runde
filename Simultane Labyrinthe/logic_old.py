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


