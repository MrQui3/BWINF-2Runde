class Move:

    def __init__(self, moves, positions, cost, heights_cost, weight=None):
        self.moves = moves
        self.positions = positions
        self.cost = cost
        self.weight = weight if weight is not None else (heights_cost - cost) / len(moves)  # moves are sorted based on this value
