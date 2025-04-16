from logic import Solving, Move
from cost import Cost
import time


def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        width, height = map(int, file.readline().split())
        data = [list(map(int, line.split())) for line in file]
    return width, height, data


def create_matrix(data, height):
    vertical_walls = [data.pop(0) for _ in range(height)]
    horizontal_walls = [data.pop(0) for _ in range(height - 1)]
    gruben_anzahl = int(data.pop(0)[0])
    gruben = [tuple(data.pop(0)) for _ in range(gruben_anzahl)]
    return horizontal_walls, vertical_walls, gruben


def create_matrix_for_laby(horizontal_walls, vertical_walls, gruben, width, height):
    cost_obj = Cost(horizontal_walls, vertical_walls, gruben, width, height)
    return cost_obj.create_cost_matrix()


def moving(cost_matrix_1, cost_matrix_2, width, height, horizontal_walls_1, vertical_walls_1, horizontal_walls_2,
           vertical_walls_2, gruben_1, gruben_2, anzahl):
    solving_obj = Solving(cost_matrix_1, cost_matrix_2, vertical_walls_1, horizontal_walls_1, vertical_walls_2,
                          horizontal_walls_2, gruben_1, gruben_2, width, height)

    moves = [Move([], ((0, 0), (0, 0)), 0, heights_cost=0, weight=0)]
    n = 0
    while True:
        n += 1
        move = moves[0]
        moves.pop(0)

        a = solving_obj.neighbours_cost(move)
        moves.extend(a)

        moves = sorted(moves, key=lambda obj: (-obj.weight, len(obj.moves)))
        moves = moves[:anzahl]  # Nur die Anzahl besten Züge speichern

        if moves[0].cost == 0:
            return moves[0], n



def main():
    start_time = time.time()

    width, height, data = read_data_from_file('labyrinthe8.txt')

    horizontal_walls_1, vertical_walls_1, gruben_1 = create_matrix(data, height)
    horizontal_walls_2, vertical_walls_2, gruben_2 = create_matrix(data, height)

    cost_matrix_1 = create_matrix_for_laby(horizontal_walls_1, vertical_walls_1, gruben_1, width, height)
    cost_matrix_2 = create_matrix_for_laby(horizontal_walls_2, vertical_walls_2, gruben_2, width, height)

    anzahl = 241
    anzahl_array = [1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 25,30, 35,40, 45, 50, 55, 65, 70, 75, 80, 85, 90, 95, 100]
    a = []
    b = []
    for i in anzahl_array:
        try:
            move, n = moving(cost_matrix_1, cost_matrix_2, width, height, horizontal_walls_1, vertical_walls_1,
                                horizontal_walls_2, vertical_walls_2, gruben_1, gruben_2, i)
            a.append(len(move.moves))
            b.append(n)
        except:
            raise
            print("No solution found")
            exit()

        print(i)
    print(a)
    print(b)

    end_time = time.time()
    print(f"Time: {end_time - start_time}")



if __name__ == "__main__":
    main()
