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

    rekursion([], solving_obj, 0)
    #solving_obj.visited = [((0, 1), (0, 0)), ((1, 0), (1, 0)), ((0, 2), (0, 0)), ((1, 1), (1, 0)), ((0, 3), (0, 0)), ((0, 2), (1, 0)), ((1, 3), (1, 0)), ((1, 2), (1, 0)), ((1, 3), (2, 0)), ((2, 2), (2, 0)), ((3, 2), (3, 0)), ((3, 1), (3, 0)), ((3, 3), (3, 1)), ((3, 0), (3, 0)), ((3, 2), (3, 1)), ((4, 0), (3, 0)), ((3, 1), (3, 1)), ((4, 1), (3, 1)), ((4, 2), (3, 1)), ((4, 1), (2, 1)), ((4, 3), (3, 1)), ((4, 2), (2, 1)), ((4, 3), (2, 2)), ((4, 2), (2, 2)), ((4, 2), (1, 2)), ((4, 3), (1, 2)), ((4, 1), (1, 1)), ((4, 1), (0, 1)), ((4, 2), (0, 2)), ((4, 3), (0, 3)), ((3, 1), (2, 1)), ((3, 0), (2, 1)), ((3, 2), (2, 2)), ((4, 0), (3, 1)), ((3, 1), (2, 2)), ((3, 1), (1, 2)), ((3, 0), (1, 1)), ((4, 0), (1, 1)), ((2, 0), (0, 1)), ((4, 1), (1, 2)), ((3, 0), (0, 1)), ((3, 1), (0, 2)), ((3, 2), (0, 3)), ((3, 2), (1, 3)), ((3, 1), (1, 3)), ((3, 2), (2, 3)), ((3, 0), (1, 3)), ((3, 1), (2, 3)), ((4, 0), (2, 3)), ((4, 1), (2, 3)), ((4, 0), (3, 3)), ((3, 0), (2, 3)), ((3, 1), (3, 3)), ((3, 0), (3, 2)), ((3, 2), (3, 3)), ((3, 1), (3, 2)), ((3, 1), (4, 2)), ((2, 0), (0, 2)), ((3, 0), (0, 2)), ((2, 0), (0, 3)), ((4, 0), (0, 2)), ((3, 1), (0, 3)), ((4, 1), (0, 3)), ((4, 2), (0, 3)), ((4, 1), (1, 3)), ((4, 2), (1, 3)), ((4, 3), (1, 3)), ((4, 2), (2, 3)), ((4, 3), (2, 3)), ((4, 2), (3, 3)), ((2, 2), (1, 2)), ((2, 2), (1, 1)), ((3, 2), (1, 1)), ((1, 2), (0, 1)), ((3, 1), (1, 1)), ((2, 2), (0, 1)), ((3, 1), (0, 1)), ((3, 2), (0, 2)), ((3, 3), (0, 3)), ((3, 3), (1, 3)), ((3, 3), (2, 3)), ((3, 3), (3, 3)), ((3, 2), (3, 2)), ((3, 2), (4, 2)), ((2, 3), (0, 2)), ((2, 3), (0, 3)), ((2, 2), (0, 2)), ((2, 3), (1, 3)), ((2, 2), (1, 3)), ((2, 3), (2, 3)), ((2, 2), (2, 3)), ((2, 3), (3, 3)), ((2, 2), (3, 2)), ((3, 3), (4, 3)), ((1, 3), (0, 2)), ((1, 3), (0, 3)), ((1, 2), (0, 2)), ((1, 3), (1, 3)), ((1, 2), (1, 3)), ((1, 3), (2, 3)), ((1, 2), (2, 3)), ((1, 3), (3, 3)), ((2, 2), (3, 3)), ((1, 2), (3, 2)), ((2, 2), (4, 2)), ((2, 3), (4, 3)), ((2, 2), (2, 1)), ((2, 3), (2, 2)), ((2, 3), (1, 2)), ((3, 3), (2, 1)), ((3, 2), (2, 1)), ((3, 3), (2, 2)), ((3, 3), (1, 2)), ((1, 2), (2, 0)), ((1, 3), (3, 0)), ((2, 2), (3, 0)), ((2, 3), (3, 1)), ((2, 3), (2, 1)), ((1, 2), (3, 0)), ((1, 3), (3, 1)), ((0, 3), (2, 1)), ((0, 3), (2, 2)), ((1, 3), (2, 2)), ((0, 3), (1, 2)), ((1, 2), (2, 1)), ((2, 2), (3, 1)), ((3, 2), (4, 1)), ((3, 1), (4, 0)), ((3, 0), (4, 0)), ((4, 0), (4, 0)), ((3, 1), (4, 1)), ((4, 1), (4, 1)), ((4, 2), (4, 1)), ((4, 3), (4, 1)), ((0, 2), (1, 1)), ((0, 2), (0, 1)), ((0, 3), (0, 2)), ((0, 3), (0, 3)), ((0, 3), (1, 0)), ((0, 2), (2, 0)), ((0, 3), (2, 0)), ((0, 2), (3, 0)), ((0, 3), (3, 1)), ((1, 3), (4, 1)), ((1, 2), (4, 0)), ((2, 2), (4, 0)), ((3, 2), (4, 0)), ((2, 3), (4, 1)), ((3, 3), (4, 1)), ((2, 1), (2, 0)), ((2, 1), (3, 0)), ((1, 1), (2, 0)), ((2, 1), (3, 1)), ((0, 1), (1, 0)), ((1, 1), (2, 1)), ((0, 1), (2, 1)), ((1, 1), (2, 2)), ((0, 2), (2, 2)), ((0, 2), (1, 2)), ((0, 1), (1, 1)), ((0, 1), (0, 1)), ((0, 2), (0, 2)), ((0, 1), (1, 2)), ((0, 0), (1, 1)), ((0, 0), (0, 1)), ((0, 1), (0, 2)), ((0, 2), (0, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 3)), ((0, 2), (2, 3)), ((0, 3), (2, 3)), ((0, 2), (3, 3)), ((0, 3), (3, 3)), ((0, 1), (3, 2)), ((0, 2), (3, 2)), ((0, 2), (4, 2)), ((0, 3), (4, 3)), ((1, 1), (4, 2)), ((1, 1), (4, 3)), ((0, 0), (0, 0)), ((1, 0), (2, 0)), ((0, 0), (1, 0)), ((1, 0), (3, 0)), ((0, 0), (2, 0)), ((1, 0), (3, 1)), ((0, 1), (2, 0)), ((1, 1), (3, 0)), ((1, 1), (3, 1)), ((0, 0), (2, 1))]
    #print(solving_obj.neighbours_cost([0, 0, 0, 3, 1, 3]))
    #print(solving_obj.visited)


smallest_solution = 10000

def rekursion(moves, solving_obj, a):
    global smallest_solution
    neighbors = solving_obj.neighbours_cost(moves)
    if a >= smallest_solution:
        return


    for i in range(len(neighbors)):
        if neighbors[i] is None:
            continue
        if neighbors[i][1] != 0:
            rekursion(neighbors[i][0], solving_obj, a+1)
        if neighbors[i][1] == 0:
            print(neighbors[i][0])
            print(a)
            smallest_solution = a

def main():
    width, height, data = read_data_from_file('labyrinthe3.txt')

    matrix_horizontal_1, matrix_vertical_1, gruben_1 = create_matrix(data, height)
    matrix_horizontal_2, matrix_vertical_2, gruben_2 = create_matrix(data, height)

    cost_matrix_1 = creating_cost_matrix(matrix_horizontal_1, matrix_vertical_1, gruben_1, width, height)
    cost_matrix_2 = creating_cost_matrix(matrix_horizontal_2, matrix_vertical_2, gruben_2, width, height)


    moving(cost_matrix_1, cost_matrix_2, width, height, matrix_horizontal_1, matrix_vertical_1, matrix_horizontal_2,
           matrix_vertical_2)


if __name__ == "__main__":
    main()
