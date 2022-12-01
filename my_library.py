class MyLibrary:
    def __init__(self):
        self._books = {}

    def add_book(self, title, author):
       self._books[title] = []
       self._books[author] = []

    def report_number_ranking(self, title, score):
       self._books[title].append(score)

    def ranking_of_books(self, title, score):
        position = self._books[title].sort(score)
        yield position

a = MyLibrary()

a.add_book('Pan Tadeusz', 'Adam Mickiewicz')
a.add_book('Lalka', 'Boleslaw Prus')
a.add_book('Nad Niemnem', 'Eliza Orzeszkowa')
a.add_book('Krzyżacy', 'Henryk Sieniewicz')

a.report_number_ranking('Pan Tadeusz', 3)
a.report_number_ranking('Lalka', 1)
a.report_number_ranking('Nad Niemnem', 2)
a.report_number_ranking('Krzyżacy', 4)

#print(a.report_number_ranking())