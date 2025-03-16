from cost import test_right, test_left, test_up, test_down

class solving:
    def __init__(self, cost_matrix_1, cost_matrix_2, vertical_matrix_1, horizontal_matrix_1,
                 vertical_matrix_2, horizontal_matrix_2, width, height):
        self.cost_matrix_1 = cost_matrix_1
        self.cost_matrix_2 = cost_matrix_2
        self.width = width
        self.height = height
        self.vertical_matrix_1 = vertical_matrix_1
        self.horizontal_matrix_1 = horizontal_matrix_1
        self.vertical_matrix_2 = vertical_matrix_2
        self.horizontal_matrix_2 = horizontal_matrix_2
        self.visited = {}
        # Funktionen und Bewegungsdeltas nur einmal definieren
        self.move_funcs = [test_right, test_left, test_up, test_down]
        self.move_deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def calculate_position(self, movements, vertical_matrix, horizontal_matrix):
        pos = (0, 0)
        mf = self.move_funcs
        md = self.move_deltas
        w = self.width
        h = self.height
        for move in movements:
            if pos == (w - 1, h - 1):
                break
            # Wähle die Matrix basierend auf der Richtung
            matrix = vertical_matrix if move < 2 else horizontal_matrix
            if mf[move](pos[0], pos[1], matrix):
                pos = (pos[0] + md[move][0], pos[1] + md[move][1])
        return pos

    def next_postion(self, at_the_moment, next_move):
        mf = self.move_funcs
        md = self.move_deltas
        pos1, pos2 = at_the_moment  # Entpacke beide Positionen
        new_pos1 = pos1
        new_pos2 = pos2

        # Für die erste Position
        matrix1 = self.vertical_matrix_1 if next_move < 2 else self.horizontal_matrix_1
        if mf[next_move](pos1[0], pos1[1], matrix1):
            new_pos1 = (pos1[0] + md[next_move][0], pos1[1] + md[next_move][1])
        # Für die zweite Position
        matrix2 = self.vertical_matrix_2 if next_move < 2 else self.horizontal_matrix_2
        if mf[next_move](pos2[0], pos2[1], matrix2):
            new_pos2 = (pos2[0] + md[next_move][0], pos2[1] + md[next_move][1])
        return new_pos1, new_pos2

    def next_move(self, pos, cost_matrix):
        w = self.width
        h = self.height
        return None if pos == (w - 1, h - 1) else cost_matrix[pos[1]][pos[0]][1]

    def get_moving_cost(self, pos, cost_matrix):
        w = self.width
        h = self.height
        return 0 if pos == (w - 1, h - 1) else cost_matrix[pos[1]][pos[0]][0]

    def get_total_cost(self, positions):
        pos1, pos2 = positions
        return self.get_moving_cost(pos1, self.cost_matrix_1) + self.get_moving_cost(pos2, self.cost_matrix_2)

    def check_visited(self, current_position, next_position, length, move):
        # Erstelle einen Schlüssel als Tupel, das beide Positionen enthält
        key = (next_position[0][0], next_position[0][1],
               next_position[1][0], next_position[1][1])
        if key in self.visited:
            return None
        self.visited[key] = length
        return move

    def neighbours_cost(self, moves):
        # Berechne beide Positionen anhand der Bewegungsfolge
        pos1 = self.calculate_position(moves, self.vertical_matrix_1, self.horizontal_matrix_1)
        pos2 = self.calculate_position(moves, self.vertical_matrix_2, self.horizontal_matrix_2)
        current_position = (pos1, pos2)

        # Ermittle den nächsten Zug für beide Positionen
        move_e = self.next_move(pos1, self.cost_matrix_1)
        move_f = self.next_move(pos2, self.cost_matrix_2)

        next_position_e = self.next_postion(current_position, move_e) if move_e is not None else None
        next_position_f = self.next_postion(current_position, move_f) if move_f is not None else None

        move_e = self.check_visited(current_position, next_position_e, len(moves) + 1, move_e) if move_e is not None else None
        move_f = self.check_visited(current_position, next_position_f, len(moves) + 1, move_f) if move_f is not None else None

        results = []
        if move_e is not None:
            results.append((moves + [move_e], self.get_total_cost(next_position_e)))
        if move_f is not None:
            results.append((moves + [move_f], self.get_total_cost(next_position_f)))
        return results
