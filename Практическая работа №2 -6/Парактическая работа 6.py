import csv

def get_books(a):
    get_book = []
    with open('books.csv', 'r', encoding='utf-8') as f:
        text = csv.reader(f, delimiter='|')
        for i in text:
            for j in i:
                b = []
                b = j.lower().split()
                if a.lower() in b:
                    print(*i)
                    get_book.append(i)
    return get_book

def get_totals(get_book):
    take = []
    take_total = []
    for i in range(len(get_book)):
        for j in range(len(get_book[i])):
            if j == 0:
                take.append(get_book[i][j])
            elif j == 3:
                total = int(get_book[i][j]) * float(get_book[i][j+1])
                take.append(total)
                if int(take[1]) < 500:
                    take[1] += int(100)
                take_total.append(take)
                take = []
                continue
    return take_total


a = input()
get_book = get_books(a)
total = print(get_totals(get_book))