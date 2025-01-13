import time


def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        teilnehmer_anzahl, stunden_anzahl, anna = file.readline().split()
        data = [list(line.split()) for line in file]
    if anna == 'y':
        raise "hast du noch nicht implementiert"

    teilnehmer_anzahl = int(teilnehmer_anzahl)
    stunden_anzahl = int(stunden_anzahl)

    formatted_data = []
    for i in range(len(data[0])):
        formatted_data.append([])
        for item in range(len(data)):
            if data[item][i] == 'y':
                formatted_data[i].append(1)
            elif data[item][i] == 'n':
                formatted_data[i].append(0)
            else:
                raise "hast du noch nicht implementiert"

    return teilnehmer_anzahl, stunden_anzahl, formatted_data


def check_line(data, line):
    was_true = False
    last_true = False
    for i in range(len(line)):
        if line[i] == 1 and not was_true:
            was_true = True
            last_true = True
        elif line[i] == 0 and was_true:
            last_true = False
        elif line[i] == 1 and was_true and not last_true:
            data_1 = data.copy()

            change_postions()
    if was_true and last_true or not was_true:
        print("Gefunden")
        exit()

def change_postions(data):
    for i in data:
        check_line(data, i)

def main():
    start_time = time.time()

    teilnehmer_anzahl, stunden_anzahl, data = read_data_from_file('konfetti00.txt')

    print(data)
    #change_postions(data)

    end_time = time.time()
    print(f"Laufzeit: {end_time - start_time} Sekunden")


if __name__ == "__main__":
    main()
