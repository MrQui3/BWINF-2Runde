import copy
from typing import Tuple

class TreeNode:

    def __init__(self, cost, parent):
        self.cost = cost
        self.children = []
        self.parent = parent
        self.is_leaf = True
        self.is_protected = False  # Wenn True, dann kann er keine kinder mehr bekommen, weil ihm bei einer imporving genommen wurde


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


def read_data_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        perl_number = int(file.readline())
        perl_sizes = [int(a) for a in file.readline().split()]
        message = file.readline()

    return perl_number, perl_sizes, message[:-1]


def create_distribution(message: str):
    characters = {}
    for char in message:
        if char in characters.keys():
            characters[char] += 1
        else:
            characters[char] = 1
    characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    return [key for key in characters.keys()], list(characters.values())


def create_tree(root: TreeNode) -> TreeNode:
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
    return total_count


def improve_tree(root:TreeNode) -> TreeNode:
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


def find_best_tree(root: TreeNode, last_cost: int) -> Tuple[TreeNode, int]:
    new_root = copy.deepcopy(root)
    new_root = improve_tree(new_root)
    new_calc = calculate_tree(new_root)
    if  new_calc > last_cost:
        return root, last_cost
    return find_best_tree(new_root, new_calc)



def main():
    root = TreeNode(0, None)
    root = create_tree(root)
    root, best_root_calc = find_best_tree(root, calculate_tree(root))
    print(best_root_calc)


if __name__ == "__main__":
    perl_number, perl_costs, message = read_data_from_file(f'schmucknachrichten/schmuck1.txt')
    characters, distribution = create_distribution(message)
    main()
