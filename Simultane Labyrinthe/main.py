from solving import solving


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


def finding_path(matrix_horizontal, matrix_vertical, gruben, width, height):
    at_the_moment = (0, 0)
    solving_obj = solving(at_the_moment, matrix_horizontal, matrix_vertical, gruben, width, height)
    while at_the_moment != (width - 1, height - 1):
        at_the_moment = solving_obj.solve(at_the_moment)
    solving_obj.stack_solving.append(at_the_moment)
    return solving_obj.create_moving_plan()



def main():
    width, height, data = read_data_from_file('labyrinthe1.txt')

    matrix_horizontal_1, matrix_vertical_1, gruben_1 = create_matrix(data, height)
    matrix_horizontal_2, matrix_vertical_2, gruben_2 = create_matrix(data, height)

    print(finding_path(matrix_horizontal_1, matrix_vertical_1, gruben_1, width, height))
    print(finding_path(matrix_horizontal_2, matrix_vertical_2, gruben_2, width, height))

if __name__ == "__main__":
    main()
