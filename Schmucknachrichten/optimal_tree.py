from decimal import Decimal


class opt:
    def __init__(self, m, array, i, depth_v):
        self.m = m
        self.array = array
        self.i = i
        self.depth_v = depth_v
        self.cost = self.calc_cost()
        self.partial_sums = self.calc_partial_sums()

    def calc_cost(self):
        cost = 0
        n = 0
        for i in range(len(self.depth_v)):
            for j in range(self.depth_v[i]):
                if n >= N:
                    return cost
                cost += V[n] * i
                n += 1

        for i in range(n, N):
            cost += self.i * V[i]
        return cost

    def caltulate_nodes(self):
        num_nodes = self.m
        for next_node in self.array:
            num_nodes += next_node
        return num_nodes

    def calc_partial_sums(self):
        partial_sums = [self.m]
        for i in range(len(self.array)):
            partial_sums.append(self.array[i] + partial_sums[i])
        return partial_sums

    def reduce(self):
        existing_nodes = self.caltulate_nodes()
        if existing_nodes > N:
            num_to_remove_nodes = N - existing_nodes

            while num_to_remove_nodes != 0:
                if self.array[-1] <= num_to_remove_nodes:
                    num_to_remove_nodes -= self.array[-1]
                    self.array.pop(-1)
                elif self.array[-1] > num_to_remove_nodes:
                    self.array[-1] -= num_to_remove_nodes
                    num_to_remove_nodes = 0


def finde_kleinstes_bei_abweichung(a):
    for spalte in range(len(a[0].partial_sums) - 1, -1, -1):
        werte = [zeile.partial_sums[spalte] for zeile in a]
        if len(set(werte)) > 1:
            kleinster_wert = min(werte)
            for zeile in a:
                if zeile.partial_sums[spalte] == kleinster_wert:
                    return zeile

    return a[0]


V = [9, 6, 5, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
N = len(V)
COST = [1, 1, 2]
D = [2, 1]

opts = [opt(0, D.copy(), 0, [0])]

possible_solutions = []

while True:

    opt_at_themoment = finde_kleinstes_bei_abweichung(opts)

    if opt_at_themoment.m >= N:
        print(opt_at_themoment.cost)
        print(opt_at_themoment.depth_v)
        print("finished")
        break

    new_cost = opt_at_themoment.cost
    for i in range(opt_at_themoment.m, N):
        new_cost += V[i]

    for i in range(1, opt_at_themoment.array[0] + 1):
        new_array = opt_at_themoment.array.copy()
        new_array.pop(0)
        new_array.append(0)

        for j in range(len(new_array)):
            new_array[j] += i * D[j]

        depth_v = opt_at_themoment.depth_v.copy()
        depth_v.append(opt_at_themoment.array[0] - i)

        a = opt(opt_at_themoment.m + opt_at_themoment.array[0] - i, new_array, opt_at_themoment.i + 1, depth_v)

        a.reduce()

        if a.m >= N:
            possible_solutions.append(a)

        if a.cost <= new_cost:
            opts.append(a)

    opts.pop(0)

    if opts == []:
        if possible_solutions == []:
            print(opt_at_themoment.m)
            print(opt_at_themoment.array)
            print("finished without solution")
        else:
            print("solution")
            print(possible_solutions)
            print()
            print()
            print()
            print()
            for a in possible_solutions:
                print(a.depth_v)
                print(a.cost)

        break
