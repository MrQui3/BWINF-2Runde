
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


perl_number, perl_costs, message = read_data_from_file(f'input/schmuck9.txt')
characters, distribution = create_distribution(message)
