dict_class = {'kid': 0, 'student': 0, 'standard': 0}

while True:
    movie = input()
    if movie == 'Finish':
        break

    places = int(input())
    bisi_places = 0

    while True:
        cls = input()

        if cls == 'End':
            break

        dict_class[cls] += 1
        bisi_places += 1

        if bisi_places == places:
            break

    print(f"{movie} - {bisi_places / places * 100:.2f}% full.")

all_tickets = sum(dict_class.values())

print(f"Total tickets: {all_tickets}")
print(f"{dict_class['student'] / all_tickets * 100:.2f}% student tickets.")
print(f"{dict_class['standard'] / all_tickets * 100:.2f}% standard tickets.")
print(f"{dict_class['kid'] / all_tickets * 100:.2f}% kids tickets.")
