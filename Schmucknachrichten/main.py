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
    root = Tree(perl_number, 0)
    while root.get_size() < len(distribution):
        root.add_child()
    return root


def fill_tree_with_data(distribution, root):
    for char in distribution:
        root.fill_tree_data(char, distribution[char])


def evaluate_tree(root):
    print(root.evaluate_tree())


def main():
    start_time = time.time()


    perl_number, perl_size, message = read_data_from_file(f'schmucknachrichten/schmuck01.txt')
    distribution = create_distribution(message)
    root = create_bin_tree(distribution, 2)
    fill_tree_with_data(distribution, root)
    evaluate_tree(root)

    end_time = time.time()
    print(f"Laufzeit: {end_time - start_time} Sekunden")


if __name__ == "__main__":
    main()
