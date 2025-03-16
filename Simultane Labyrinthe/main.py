import math
from logic import *
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


def solving_labyrinth(cost_matrix_1, cost_matrix_2, matrix_vertical_1, matrix_horizontal_1, matrix_vertical_2, matrix_horizontal_2, width, height):
    way = []
    while True:
        sequenz_1 = create_sequenz(cost_matrix_1, calculate_position(way, matrix_vertical_1, matrix_horizontal_1, width, height))
        sequenz_2 = create_sequenz(cost_matrix_2, calculate_position(way, matrix_vertical_2, matrix_horizontal_2, width, height))

        if len(sequenz_1) == 0 and len(sequenz_2) == 0:
            break

        if sequenz_1[0] == sequenz_2[0]:
            # Beide empfehlen die gleiche Richtung
            way.append(sequenz_1[0])
            continue

        a = calculate_next_move(sequenz_1, sequenz_2)
        if a is None:
            break
        way.append(a)

    print(way)



def main():
    start_time = time.time()

    width, height, data = read_data_from_file('labyrinthe2.txt')

    matrix_horizontal_1, matrix_vertical_1, gruben_1 = create_matrix(data, height)
    matrix_horizontal_2, matrix_vertical_2, gruben_2 = create_matrix(data, height)

    cost_matrix_1 = creating_cost_matrix(matrix_horizontal_1, matrix_vertical_1, gruben_1, width, height)
    cost_matrix_2 = creating_cost_matrix(matrix_horizontal_2, matrix_vertical_2, gruben_2, width, height)

    solving_labyrinth(cost_matrix_1, cost_matrix_2, matrix_vertical_1, matrix_horizontal_1, matrix_vertical_2, matrix_horizontal_2, width, height)


    end_time = time.time()
    print(f"Laufzeit: {end_time - start_time} Sekunden")


if __name__ == "__main__":
    main()
