import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from logic import solving
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
    gruben = [data.pop(0) for _ in range(gruben_anzahl)]
    return matrix_horizontal, matrix_vertical, gruben


def creating_cost_matrix(matrix_horizontal, matrix_vertical, gruben, width, height):
    solving_obj = cost(matrix_horizontal, matrix_vertical, gruben, width, height)
    return solving_obj.create_cost_matrix()


def moving(cost_matrix_1, cost_matrix_2, width, height, matrix_horizontal_1, matrix_vertical_1, matrix_horizontal_2,
           matrix_vertical_2, anzahl):
    solving_obj = solving(cost_matrix_1, cost_matrix_2, matrix_vertical_1, matrix_horizontal_1, matrix_vertical_2,
                          matrix_horizontal_2, width, height)
    heighest_cost = cost_matrix_1[0][0][0] + cost_matrix_2[0][0][0]
    moves = [([], heighest_cost)]
    n = 0
    while True:
        n += 1
        try:
            a = solving_obj.neighbours_cost(moves[0][0])
            moves.pop(0)
            moves.extend(a)
            moves.sort(key=lambda x: (heighest_cost - x[1]) / len(x[0]) if len(x[0]) > 0 else float('-inf'),
                       reverse=True)
            moves = moves[:anzahl]  # Nur die 1000 besten Züge speichern
            if moves[0][1] == 0:
                return moves[0][0], n

        except:
            print(anzahl)
            return 'No solution', n


def main():
    start_time = time.time()

    width, height, data = read_data_from_file(f'labyrinthe8.txt')

    matrix_horizontal_1, matrix_vertical_1, gruben_1 = create_matrix(data, height)
    matrix_horizontal_2, matrix_vertical_2, gruben_2 = create_matrix(data, height)

    cost_matrix_1 = creating_cost_matrix(matrix_horizontal_1, matrix_vertical_1, gruben_1, width, height)
    cost_matrix_2 = creating_cost_matrix(matrix_horizontal_2, matrix_vertical_2, gruben_2, width, height)

    anzahl = 1
    anzahl_array = []
    moves_array = []
    iterations_array = []
    for i in range(10):
        moves, n = moving(cost_matrix_1, cost_matrix_2, width, height, matrix_horizontal_1, matrix_vertical_1,
                          matrix_horizontal_2, matrix_vertical_2, anzahl)
        if moves == 'No solution':
            continue
        anzahl_array.append(anzahl)
        moves_array.append(len(moves))
        iterations_array.append(n)
        anzahl += 30

    print(anzahl_array)
    print(moves_array)
    print(iterations_array)
    plt.plot(anzahl_array, moves_array, marker='', linestyle='-', color='b')
    plt.grid(True)
    plt.show()
    plt.plot(anzahl_array, iterations_array, marker='', linestyle='-', color='b')
    plt.grid(True)
    plt.show()

    end_time = time.time()
    print(f"Time: {end_time - start_time}")


if __name__ == "__main__":
    main()
