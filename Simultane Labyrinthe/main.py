from logic import cost, solving


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
           matrix_vertical_2):
    solving_obj = solving(cost_matrix_1, cost_matrix_2, matrix_vertical_1, matrix_horizontal_1, matrix_vertical_2,
                          matrix_horizontal_2, width, height)
    moves = [[[], 3, 0]]  # Initialisiere die Bewegungen
    iteration_count = 0

    while True:
        # Finde das beste Element aus der Liste
        current = min(moves, key=lambda x: (x[2], x[1]))
        if current[1] <= 2:  # Abbruchbedingung
            break

        iteration_count += 1
        moves.remove(current)
        # Berechne die Kosten für Nachbarn
        neighbours = solving_obj.neighbours_cost(current[0])
        for i in range(4):
            moves.append([current[0] + [i], neighbours[i], neighbours[i] - current[1]])

    # Ergebnis ausgeben
    print(current)
    print(iteration_count)


def main():
    width, height, data = read_data_from_file('labyrinthe3.txt')

    matrix_horizontal_1, matrix_vertical_1, gruben_1 = create_matrix(data, height)
    matrix_horizontal_2, matrix_vertical_2, gruben_2 = create_matrix(data, height)

    cost_matrix_1 = creating_cost_matrix(matrix_horizontal_1, matrix_vertical_1, gruben_1, width, height)
    cost_matrix_2 = creating_cost_matrix(matrix_horizontal_2, matrix_vertical_2, gruben_2, width, height)

    moving(cost_matrix_1, cost_matrix_2, width, height, matrix_horizontal_1, matrix_vertical_1, matrix_horizontal_2, matrix_vertical_2)


if __name__ == "__main__":
    main()
