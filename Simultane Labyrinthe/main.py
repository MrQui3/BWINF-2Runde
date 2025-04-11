from logic import solving, Move
from cost import cost
import time


def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        width, height = map(int, file.readline().split())
        data = [list(map(int, line.split())) for line in file]
    return width, height, data


def create_matrix(data, height):
    matrix_vertical = [data.pop(0) for _ in range(height)]
    matrix_horizontal = [data.pop(0) for _ in range(height - 1)]
    gruben_anzahl = int(data.pop(0)[0])
    gruben = [tuple(data.pop(0)) for _ in range(gruben_anzahl)]
    return matrix_horizontal, matrix_vertical, gruben


def creating_cost_matrix(matrix_horizontal, matrix_vertical, gruben, width, height):
    solving_obj = cost(matrix_horizontal, matrix_vertical, gruben, width, height)
    return solving_obj.create_cost_matrix()


def moving(cost_matrix_1, cost_matrix_2, width, height, matrix_horizontal_1, matrix_vertical_1, matrix_horizontal_2,
           matrix_vertical_2, gruben_1, gruben_2, anzahl):
    solving_obj = solving(cost_matrix_1, cost_matrix_2, matrix_vertical_1, matrix_horizontal_1, matrix_vertical_2,
                          matrix_horizontal_2, gruben_1, gruben_2, width, height)

    moves = [Move([], ((0, 0), (0, 0)), 0, heights_cost=0, weight=0)]
    n = 0
    while True:
        n += 1
        a = solving_obj.neighbours_cost(moves[0])
        moves.pop(0)
        moves.extend(a)

        moves = sorted(moves, key=lambda obj: (-obj.weight, len(obj.moves)))
        moves = moves[:anzahl]  # Nur die Anzahl besten Züge speichern

        if moves[0].cost == 0:
            return moves[0], n



def main():
    start_time = time.time()

    width, height, data = read_data_from_file('Simultane Labyrinthe/labyrinthe6.txt')

    matrix_horizontal_1, matrix_vertical_1, gruben_1 = create_matrix(data, height)
    matrix_horizontal_2, matrix_vertical_2, gruben_2 = create_matrix(data, height)

    cost_matrix_1 = creating_cost_matrix(matrix_horizontal_1, matrix_vertical_1, gruben_1, width, height)
    cost_matrix_2 = creating_cost_matrix(matrix_horizontal_2, matrix_vertical_2, gruben_2, width, height)
    print("finsid costmatrix")

    anzahl = 1000
    move, n = moving(cost_matrix_1, cost_matrix_2, width, height, matrix_horizontal_1, matrix_vertical_1,
                          matrix_horizontal_2, matrix_vertical_2, gruben_1, gruben_2, anzahl)

    print(move.moves)
    print(n)
    print(len(move.moves))

    end_time = time.time()
    print(f"Time: {end_time - start_time}")



if __name__ == "__main__":
    main()
