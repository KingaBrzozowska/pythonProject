import csv
#import pandas from pd
from typing import NamedTuple


class Book(NamedTuple):
    id: int
    title: str
    author: str
    ranking: int

c1 = Book(1, 'Pan Tadeusz', 'Adam Mickiewicz', 2)
c2 = Book(2, 'Lalka', 'Boleslaw Prus', 3)
c3 = Book(3, 'Nad Niemnem', 'Eliza Orzeszkowa', 1)
c4 = Book(4, 'Krzyżacy', 'Henryk Sienkiewicz', 5)
c5 = Book(5, 'Potop', 'Henryk Sienkiewicz', 6)
c6 = Book(6, 'Pan Wołodyjowski', 'Henryk Sienkiewicz', 4)
c7 = Book(7, 'Ferdydurke', 'Witold Gombrowicz', 7)

books = [c1, c2, c3, c4, c5, c6, c7]

books.sort(key=lambda e: e.ranking) #sortuje wg miejsca w rankingu

#zapisuje do pliku books.csv wszytskie pozycje z książkami
with open('books.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(c1)
    writer.writerow(c2)
    writer.writerow(c3)
    writer.writerow(c4)
    writer.writerow(c5)
    writer.writerow(c6)
    writer.writerow(c7)

# wyświetla listę wszystkich książek wg miejsca w rankingu
for book in books:
    print(book)


