import copy
from treenode import TreeNode
from load_input import distribution, characters


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


def improve_tree(root: TreeNode) -> TreeNode:
    all_leaves = root.get_leaves()
    all_leaves = sorted(all_leaves, key=lambda x: (x.cost, len(x.parent.children)))
    highest_cost = 0
    parent_node = None
    for i in range(len(all_leaves)):
        if all_leaves[i].parent.parent is not None:
            if all_leaves[i].cost * distribution[i] > highest_cost:
                highest_cost = all_leaves[i].cost * distribution[i]
                parent_node = all_leaves[i].parent

    parent_node.is_leaf = True
    parent_node.children = []
    parent_node.is_protected = True

    return create_tree(root)


def find_best_tree(root):
    best_value = calculate_tree(root)
    best_root = copy.deepcopy(root)
    while True:
        try:
            root = improve_tree(root)
            new_calc = calculate_tree(root)

            if new_calc < best_value:
                best_value = new_calc
                best_root = copy.deepcopy(root)
        except Exception as e:
            # Gibt keine Verbesserung mehr
            return best_root


def output(root):
    print(f"Gesamtkosten: {calculate_tree(root)}")
    all_leaves = root.get_leaves()
    all_leaves = sorted(all_leaves, key=lambda x: (x.cost, len(x.parent.children)))
    for i in range(len(all_leaves)):
        print(f"{characters[i]}: {all_leaves[i].perl_code}")


def main():
    # Initiiere Wurzel objekt
    root = TreeNode(0, None, [])

    # Erstellen des balancierten Baums
    root = create_tree(root)

    # Verbessern des Baums
    root = find_best_tree(root)
    output(root)



if __name__ == "__main__":
    main()
