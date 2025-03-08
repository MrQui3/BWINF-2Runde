import time
from tree import Tree, Data
import copy
import random


def read_data_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        perl_number = int(file.readline())
        perl_sizes = [int(a) for a in file.readline().split()]
        message = file.readline()

    return perl_number, perl_sizes, message[:-1]


def create_distribution(message):
    characters = {}
    for char in message:
        if char in characters.keys():
            characters[char] += 1
        else:
            characters[char] = 1
    characters = dict(sorted(characters.items(), key=lambda item: item[1]))
    return characters


def create_bin_tree(distribution_length, perl_number, children_cost):
    root = Tree(perl_number, None, 0, children_cost, 0)
    while root.get_size() < distribution_length:
        root.add_child(-1)
    return root


def fill_tree_with_data(distribution, root):
    for char in distribution:
        cost, node = root.get_highest_cost(0)
        node.data_structure = Data(char, distribution[char])


def find_smallest(distribution, perl_number, children_cost):
    root = create_bin_tree(len(distribution), perl_number, children_cost)
    fill_tree_with_data(distribution, root)
    last_value = root.evaluate_tree()
    while True:
        last_root = copy.deepcopy(root)

        _, to_delete = root.get_highest_value(0)
        number_of_children = to_delete.get_size()
        root.delete_node(to_delete)
        for _ in range(number_of_children-1):
            root.add_child(to_delete.cost)

        fill_tree_with_data(distribution, root)
        root_value = root.evaluate_tree()

        if last_value < root_value or root.get_size() != len(distribution):
            return last_root.return_graph()
        last_value = root_value


def dict_to_list(dictionary):
    return sorted(list(dictionary.values()), reverse=True)



def main():
    start_time = time.time()

    perl_number, perl_size, message = read_data_from_file(f'schmucknachrichten/schmuck1.txt')
    distribution = create_distribution(message)
    print(dict_to_list(distribution))
    print(len(distribution))
    print(perl_size)
    solution = find_smallest(distribution, perl_number, perl_size)
    a = 0
    for node in solution:
        print(solution[node])
        print(distribution[node])
        print()
        for i in solution[node]:
            a += perl_size[i]*distribution[node]
    print(a)

    end_time = time.time()
    print(f"Laufzeit: {end_time - start_time} Sekunden")


if __name__ == "__main__":
    main()
