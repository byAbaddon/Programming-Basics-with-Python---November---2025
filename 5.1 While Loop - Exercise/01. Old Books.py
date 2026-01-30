book_name = input()
c = 0

while True:
    book = input()
    if book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {c} books.')
        break
    if book_name == book:
        print(f'You checked {c} books and found it.')
        break
    c += 1
