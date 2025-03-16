from cost import cost
from cost import test_up, test_down, test_left, test_right


def creating_cost_matrix(matrix_horizontal, matrix_vertical, gruben, width, height):
    solving_obj = cost(matrix_horizontal, matrix_vertical, gruben, width, height)
    return solving_obj.create_cost_matrix()


def create_sequenz(cost_matrix, position):
    sequenz = []
    move_deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for i in range(13):
        position_cost = cost_matrix[position[1]][position[0]]
        if position_cost[1] == None:
            break
        position = (position[0] + move_deltas[position_cost[1]][0], position[1] + move_deltas[position_cost[1]][1])
        sequenz.append(position_cost[1])
    return sequenz


def calculate_position(movements, vertical_matrix, horizontal_matrix, width, height):
    at_the_moment = (0, 0)
    move_funcs = [test_right, test_left, test_up, test_down]
    move_deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for move in movements:
        if at_the_moment == (width - 1, height - 1):
            break
        if move_funcs[move](at_the_moment[0], at_the_moment[1], vertical_matrix if move < 2 else horizontal_matrix):
            at_the_moment = (at_the_moment[0] + move_deltas[move][0], at_the_moment[1] + move_deltas[move][1])

    return at_the_moment


def next_common_substrings(seq1, seq2, min_length=2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if seq1[i] == seq2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                length = dp[i + 1][j + 1]
                start1 = i - length + 1
                start2 = j - length + 1

                if length >= min_length:
                    common_substr = tuple(seq1[start1:i + 1])
                    prefix_seq1 = tuple(seq1[:start1]) if start1 > 0 else ()
                    prefix_seq2 = tuple(seq2[:start2]) if start2 > 0 else ()

                    return prefix_seq1, prefix_seq2, common_substr

    return None, None, None  # Falls keine Sequenz gefunden wird


def calculate_next_move(sequenz_1, sequenz_2):
    prefix_seq1, prefix_seq2, common_subsequenz = next_common_substrings(sequenz_1, sequenz_2)

    if prefix_seq1 is None:
        return None

    if len(prefix_seq1) != 0 and len(prefix_seq2) != 0:
        return prefix_seq2[0] if len(prefix_seq1) < len(prefix_seq2) else prefix_seq1[0]

    if len(prefix_seq1) == 0:
        return prefix_seq2[0]
    if len(prefix_seq2) == 0:
        return prefix_seq1[0]

