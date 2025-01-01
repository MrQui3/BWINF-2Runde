class solving:

    def __init__(self, at_the_moment, horizontal_matrix, vertical_matrix, gruben, width, height):
        self.stack_solving = []
        self.markedVisited = []
        self.horizontal_matrix = horizontal_matrix
        self.vertical_matrix = vertical_matrix
        self.gruben = gruben
        self.width = width
        self.height = height

    def get_neighbors(self, x, y):
        neighbors = []
        if x > 0:
            if (x - 1, y) not in self.markedVisited and self.vertical_matrix[y][x-1] == 0:
                neighbors.append((x - 1, y))
        if x < self.width-1:
            if (x + 1, y) not in self.markedVisited and self.vertical_matrix[y][x] == 0:
                neighbors.append((x + 1, y))
        if y > 0:
            if (x, y - 1) not in self.markedVisited and self.horizontal_matrix[y-1][x] == 0:
                neighbors.append((x, y - 1))
        if y < self.height-1:
            if (x, y + 1) not in self.markedVisited and self.horizontal_matrix[y][x] == 0:
                neighbors.append((x, y + 1))
        return neighbors

    def solve(self, at_the_moment):
        if at_the_moment not in self.markedVisited:
            self.markedVisited.append(at_the_moment)
            self.stack_solving.append(at_the_moment)
        neighbors = self.get_neighbors(at_the_moment[0], at_the_moment[1])
        if len(neighbors) == 0:
            self.stack_solving.pop(-1)
            return self.stack_solving[-1]
        return neighbors[0]

    def create_moving_plan(self):
        # 0 = right, 1 = left, 2 = up, 3 = down
        moving_plan = []
        for i in range(len(self.stack_solving) - 1):
            if self.stack_solving[i][0] == self.stack_solving[i + 1][0]:
                if self.stack_solving[i][1] < self.stack_solving[i + 1][1]:
                    moving_plan.append(3)
                else:
                    moving_plan.append(2)
            else:
                if self.stack_solving[i][0] < self.stack_solving[i + 1][0]:
                    moving_plan.append(0)
                else:
                    moving_plan.append(1)
        return moving_plan
