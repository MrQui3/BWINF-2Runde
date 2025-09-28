from solve import Solving
from move import Move
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
           vertical_walls_2, gruben_1, gruben_2, l):
    
    
    solving_obj = Solving(cost_matrix_1, cost_matrix_2, vertical_walls_1, horizontal_walls_1, vertical_walls_2,
                          horizontal_walls_2, gruben_1, gruben_2, width, height)

    moves = [Move([], ((0, 0), (0, 0)), 0, heights_cost=0, weight=0)]
    while True:

        # Erstes Element aus der Liste nehmen
        move = moves[0]
        moves.pop(0)

        # Liste mit den neuen Wegen erweitern
        new_moves = solving_obj.neighbours_cost(move)
        moves.extend(new_moves)

        moves = sorted(moves, key=lambda obj: (-obj.weight, len(obj.moves)))
        moves = moves[:l]  # Nur die l besten Züge speichern

        if moves[0].cost == 0:
            return moves[0]


def output(move):
    print(len(move.moves))
    #print(move.moves)


def main():
    # Datei Einlesen
    width, height, data = read_data_from_file('labyrinthe8.txt')

    # Listen erstellen
    horizontal_walls_1, vertical_walls_1, gruben_1 = create_matrix(data, height)
    horizontal_walls_2, vertical_walls_2, gruben_2 = create_matrix(data, height)

    # Matrix für beide Labyrinthe erstellen
    cost_matrix_1 = create_matrix_for_laby(horizontal_walls_1, vertical_walls_1, gruben_1, width, height)
    cost_matrix_2 = create_matrix_for_laby(horizontal_walls_2, vertical_walls_2, gruben_2, width, height)

    # Weg finden
    start = time.time()
    # TODO: Wert für l anpassen
    l = 10000
    try:
        move = moving(cost_matrix_1, cost_matrix_2, width, height, horizontal_walls_1, vertical_walls_1,
                            horizontal_walls_2, vertical_walls_2, gruben_1, gruben_2, l)
        output(move)

    except:
        print("No solution found")
    print(f"Time taken: {time.time() - start:.2f} seconds")



if __name__ == "__main__":
    main()
