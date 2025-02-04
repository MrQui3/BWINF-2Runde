import math
import time
from tree import Tree


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


def create_bin_tree(distribution, perl_number):
    root = Tree(perl_number, None, 0)
    while root.get_size() < len(distribution):
        root.add_child()
    return root


def fill_tree_with_data(distribution, root):
    for char in distribution:
        root.fill_tree_data(char, distribution[char])

def find_smallest(distribution, perl_number):
    root = create_bin_tree(distribution, perl_number)
    fill_tree_with_data(distribution, root)
    c = root.evaluate_tree()
    d = c-1
    print(c)
    while d < c:
        c = d
        a, to_delete = root.get_highest_value(0)
        b = to_delete.get_size()
        root.delete_node(to_delete)
        root.insert_new_node(b)
        fill_tree_with_data(distribution, root)
        d = root.evaluate_tree()

    return c



def main():
    start_time = time.time()

    perl_number, perl_size, message = read_data_from_file(f'schmucknachrichten/schmuck4.txt')
    distribution = create_distribution(message)
    #distribution = {'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 6, 'f': 8, 'g': 10, 'h': 12}
    #perl_number = 2

    print(find_smallest(distribution, perl_number))

    end_time = time.time()
    print(f"Laufzeit: {end_time - start_time} Sekunden")


if __name__ == "__main__":
    main()
