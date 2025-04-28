from load_input import perl_costs


class TreeNode:

    def __init__(self, cost, parent, perl_code):
        self.perl_code = perl_code  # Speichert die Codierung für den Knoten
        self.cost = cost
        self.children = []
        self.parent = parent
        self.is_leaf = True
        self.is_protected = False  # Wenn True, dann kann er keine kinder mehr bekommen

    def insert_new_node(self, obj):
        if obj is self:
            if self.is_leaf:  # Damit jede parent immer mehr mindestens zwei kinder hat
                self.is_leaf = False
                self.children.append(TreeNode(self.cost + perl_costs[0], self, self.perl_code+[len(self.children)]))

            self.children.append(TreeNode(self.cost + perl_costs[len(self.children)], self, self.perl_code+[len(self.children)]))
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

        children_leaves = []
        for child in self.children:
            for i in child.get_leaves():
                children_leaves.append(i)
        return children_leaves

    def get_all_possible_costs(self) -> dict:
        children_cost = {}
        if len(self.children) < len(perl_costs) and self.is_protected is False:
            if self.is_leaf:
                children_cost[self] = self.cost + perl_costs[0] + self.cost + perl_costs[1]
            else:
                children_cost[self] = self.cost + perl_costs[len(self.children)]

        for child in self.children:
           children_cost.update(child.get_all_possible_costs())
        return children_cost

    def get_internal_nodes(self):
        if self.is_leaf:
            return 0
        return sum(child.get_interal_nodes() for child in self.children) + 1
