class RevealAccess(object):
    """Deskryptor danych, który ustawia i zwraca wartości w standardowy sposób
    oraz wyświetla komunikat z informacją o dostępie do wartości.
    """

    def __init__(self, initval=None, name="var"):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Pobieranie", self.name)
        return self.val

    def __set__(self, obj, val):
        print("Aktualizowanie", self.name)
        self.val = val

    def __delete__(self, obj):
        print("Usuwanie", self.name)


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5