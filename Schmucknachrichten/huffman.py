from huffman_tree import Tree


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


def create_new_node(working_list, perl_size):
    children = []
    cost = 0
    for i in range(perl_size):
        if len(working_list) == 0:
            break
        children.append(working_list[0])
        cost += working_list[0].cost
        working_list.pop(0)
    return Tree(children, cost), working_list


def createTree(distribution, perl_sizes):
    working_list = []
    for char in distribution:
        working_list.append(Tree(None, distribution[char]))

    while len(working_list) > 1:
        new_node, working_list = create_new_node(working_list, perl_sizes)
        working_list.append(new_node)
        working_list = sorted(working_list, key=lambda node: node.cost)

    return working_list[0]


def create_cost(a, increment):
    if a.children is None:
        return a.cost*increment

    b = 0
    for child in a.children:
        b += create_cost(child, increment+1)
    return b

def main():

    perl_number, perl_size, message = read_data_from_file(f'schmucknachrichten/schmuck6.txt')
    distribution = create_distribution(message)

    a = createTree(distribution, perl_number)

    print(create_cost(a, 0))


if __name__ == "__main__":
    main()
