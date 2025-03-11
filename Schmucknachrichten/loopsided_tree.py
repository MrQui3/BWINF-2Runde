class TreeNode:

    def __init__(self, cost, parent):
        self.cost = cost
        self.children = []
        self.parent = parent
        self.is_leaf = True
        self.possible_children_cost = self.get_possible_children()
        self.is_protected = False  # Wenn True, dann kann er keine kinder mehr bekommen, weil ihm bei einer imporving genommen wurde

    def get_possible_children(self):
        children = []
        for i in range(len(perl_costs)):
            children.append(self.cost + perl_costs[i])
        return children

    def insert_new_node(self, obj):
        if obj is self:
            if self.is_leaf:  # Damit jede parent immer mehr mindestens zwei kinder hat
                self.is_leaf = False
                self.children.append(TreeNode(self.cost + perl_costs[0], self))

            self.children.append(TreeNode(self.cost + perl_costs[len(self.children)], self))
            return

        for child in self.children:
            child.insert_new_node(obj)

    def get_size(self) -> int:
        if self.is_leaf:
            return 1
        return sum(child.get_size() for child in self.children)

    def get_leaves(self) -> list:
        if self.is_leaf:
            return [self]

        a = []
        for child in self.children:
            for i in child.get_leaves():
                a.append(i)
        return a

    def get_all_possible_costs(self) -> dict:
        a = {}
        if len(self.children) < len(perl_costs) and self.is_protected is False:
            if self.is_leaf:
                a[self] = self.cost + perl_costs[0] + perl_costs[1]
            else:
                a[self] = self.cost + perl_costs[len(self.children)]

        for child in self.children:
            a.update(child.get_all_possible_costs())
        return a


def create_tree(root):
    while root.get_size() < len(distribution):
        possible_children = root.get_all_possible_costs()
        smallest_value = min(possible_children.items(), key=lambda item: item[1])

        root.insert_new_node(smallest_value[0])
    return root


def calculate_tree(root):
    all_leaves = root.get_leaves()
    all_leaves = sorted(all_leaves, key=lambda x: (x.cost, len(x.parent.children)))
    total_count = 0
    for i in range(len(all_leaves)):
        total_count += all_leaves[i].cost * distribution[i]
    print(total_count)


def improve_tree(root):
    all_leaves = root.get_leaves()
    all_leaves = sorted(all_leaves, key=lambda x: (x.cost, len(x.parent.children)))
    a = 0
    b = None
    for i in range(len(all_leaves)):
        if all_leaves[i].parent.parent is not None:
            if all_leaves[i].cost * distribution[i] > a:
                a = all_leaves[i].cost * distribution[i]
                b = all_leaves[i].parent

    b.is_leaf = True
    b.children = []
    b.is_protected = True

    return create_tree(root)


distribution = [173, 139, 138, 126, 123, 119, 112, 111, 108, 105, 89, 83, 81, 79, 72, 72, 68, 67, 61, 61, 60, 52, 46, 46, 42, 39, 36, 35, 33, 31, 31, 30, 30, 29, 27, 26, 26, 26, 25, 23, 23, 23, 22, 20, 20, 20, 18, 18, 18, 17, 17, 17, 17, 17, 16, 16, 15, 15, 15, 14, 14, 14, 13, 13, 13, 13, 12, 12, 12, 11, 11, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
perl_costs = [1, 2, 3, 4]

root = TreeNode(0, None)
root = create_tree(root)
calculate_tree(root)


for i in range(60):
    root = improve_tree(root)
    calculate_tree(root)

