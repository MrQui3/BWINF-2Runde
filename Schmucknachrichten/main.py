import time


def read_data_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        perl_number = int(file.readline())
        perl_sizes = [int(a) for a in file.readline().split()]
        message = file.readline()

    return perl_number, perl_sizes, message


def create_distribution(message):
    characters = {}
    for char in message:
        if char in characters.keys():
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def main():
    start_time = time.time()

    perl_number, perl_size, message = read_data_from_file(f'schmucknachrichten/schmuck{i}.txt')

    distribution = create_distribution(message)

    end_time = time.time()
    print(f"Laufzeit: {end_time - start_time} Sekunden")


if __name__ == "__main__":
    main()
