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
    moves = [[[], (cost_matrix_1[0][0] + cost_matrix_2[0][0]), 0, []]]  # Initialisiere die Bewegungen
    iteration_count = 0

    print(solving_obj.neighbours_cost([3, 3, 0, 2, 2, 0, 3, 3]))

    neighbors = solving_obj.neighbours_cost(moves[0][0])
    #rekursion(moves[0][0] + [3], solving_obj, neighbors[0][0])
    for i in range(len(neighbors)):
        if neighbors[i][0] < 16:
            #rekursion(moves[0][0] + [i], solving_obj, neighbors[i][0])
            pass


def rekursion(moves, solving_obj, last_int):
    neighbors = solving_obj.neighbours_cost(moves)
    for i in range(len(neighbors)):
        if neighbors[i][0] != 0 and neighbors[i][0] < last_int:
            rekursion(moves + [i], solving_obj, neighbors[i][0])
        print(moves + [i])


def main():
    width, height, data = read_data_from_file('labyrinthe0.txt')

    matrix_horizontal_1, matrix_vertical_1, gruben_1 = create_matrix(data, height)
    matrix_horizontal_2, matrix_vertical_2, gruben_2 = create_matrix(data, height)

    cost_matrix_1 = creating_cost_matrix(matrix_horizontal_1, matrix_vertical_1, gruben_1, width, height)
    cost_matrix_2 = creating_cost_matrix(matrix_horizontal_2, matrix_vertical_2, gruben_2, width, height)

    moving(cost_matrix_1, cost_matrix_2, width, height, matrix_horizontal_1, matrix_vertical_1, matrix_horizontal_2,
           matrix_vertical_2)


if __name__ == "__main__":
    main()
