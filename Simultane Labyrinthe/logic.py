from cost import test_right, test_left, test_up, test_down


class Move:

    def __init__(self, moves, positions, cost, heights_cost, weight=None):
        self.moves = moves
        self.positions = positions
        self.cost = cost
        self.weight = weight if weight is not None else (heights_cost - cost) / len(moves)  # moves are sorted based on this value


class Solving:
    def __init__(self, cost_matrix_1, cost_matrix_2, vertical_walls_1, horizontal_walls_1,
                 vertical_walls_2, horizontal_walls_2, gruben_1, gruben_2, width, height):
        self.width = width
        self.height = height
        self.cost_at_beginning = cost_matrix_1[0][0][0] + cost_matrix_2[0][0][0]

        self.gruben_1 = gruben_1
        self.gruben_2 = gruben_2

        self.vertical_walls_1 = vertical_walls_1
        self.horizontal_walls_1 = horizontal_walls_1

        self.vertical_walls_2 = vertical_walls_2
        self.horizontal_walls_2 = horizontal_walls_2

        self.cost_matrix_1 = cost_matrix_1
        self.cost_matrix_2 = cost_matrix_2

        self.visited = {}
        # Funktionen und Bewegungsdeltas nur einmal definieren
        self.move_funcs = [test_right, test_left, test_up, test_down]
        self.move_deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def next_postion(self, position, next_move):
        mf = self.move_funcs
        md = self.move_deltas
        pos1 = position[0]
        pos2 = position[1]

        # Für die erste Position
        if pos1 != (self.width - 1, self.height - 1):
            matrix1 = self.vertical_walls_1 if next_move < 2 else self.horizontal_walls_1
            if mf[next_move](pos1[0], pos1[1], matrix1):
                pos1 = (pos1[0] + md[next_move][0], pos1[1] + md[next_move][1])
                if pos1 in self.gruben_1:
                    pos1 = (0, 0)

        # Für die zweite Position
        if pos2 != (self.width - 1, self.height - 1):
            matrix2 = self.vertical_walls_2 if next_move < 2 else self.horizontal_walls_2
            if mf[next_move](pos2[0], pos2[1], matrix2):
                pos2 = (pos2[0] + md[next_move][0], pos2[1] + md[next_move][1])
                if pos2 in self.gruben_2:
                    pos2 = (0, 0)
        return pos1, pos2

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

    def check_visited(self, next_position, length, move):
        # Erstelle einen Schlüssel als Tupel, das beide Positionen enthält
        key = (next_position[0][0], next_position[0][1],
               next_position[1][0], next_position[1][1])
        if key in self.visited and self.visited[key] <= length:
            return None
        self.visited[key] = length
        return move

    def neighbours_cost(self, move: Move):
        # Berechne beide Positionen anhand der Bewegungsfolge
        pos1 = move.positions[0]
        pos2 = move.positions[1]

        # Ermittle den nächsten Zug für beide Positionen
        move_e = self.next_move(pos1, self.cost_matrix_1)
        move_f = self.next_move(pos2, self.cost_matrix_2)

        next_position_e = self.next_postion(move.positions, move_e) if move_e is not None else None
        next_position_f = self.next_postion(move.positions, move_f) if move_f is not None else None

        
        move_e = self.check_visited(next_position_e, len(move.moves) + 1, move_e) if move_e is not None else None
        move_f = self.check_visited(next_position_f, len(move.moves) + 1, move_f) if move_f is not None else None

        results = []
        if move_e is not None:
            results.append(Move(move.moves + [move_e], next_position_e, self.get_total_cost(next_position_e), self.cost_at_beginning))
        if move_f is not None:
            results.append(Move(move.moves + [move_f], next_position_f, self.get_total_cost(next_position_f), self.cost_at_beginning))
        return results
