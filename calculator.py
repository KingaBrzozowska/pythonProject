from datetime import datetime
from typing import Any
from functools import singledispatch, singledispatchmethod
import report

# Próbowałam uzyć tej metody, ale niestety miałam błąd:
# AttributeError: module 'report' has no attribute 'register'
#
# class Example:
#     @singledispatchmethod
#     def method(self, argument):
#         pass
#
#     @method.register
#     def _(self, argument: float):
#         pass
#
#
# @report.register
# def _(value: datetime):
#      return f'Obiekt datetime: {value.isoformat()}'

print(f'Data:', datetime.now())

def calculate():
    operation = input('''
Wprowadź numer działania, które chcesz wykonać (1-4):
(1) DODAWANIE
(2) ODEJMOWANIE
(3) MNOŻENIE
(4) DZIELENIE
''')
    number_1 = int(input('Wprowadź pierwszą liczbę: '))
    number_2 = int(input('Wprowadź drugą liczbę: '))

    if operation == '1':
        print(number_1, "+", number_2, "=", number_1 + number_2)

    elif operation == '2':
        print(number_1, "-", number_2, "=", number_1 - number_2)

    elif operation == '3':
        print(number_1, "*", number_2, "=", number_1 * number_2)

    elif operation == '4':
        try:
            wynik = number_1 / number_2
        except Exception as e:
            print("Nieprawidłowe dane:", e.args)
            return 0
        else:
            print(number_1, "/", number_2, "=", number_1 / number_2)
            return wynik

    else:
        print('Błędny wybór operacji działania. Spróbuj jeszcze raz!')

def again():
    calc_again = input('''
Czy chcesz coś jeszcze obliczyć? 
Wybierz T jeśli TAK, N jak chcesz zakończyć pracę z kalkulatorem.
''')

    if calc_again.upper() == 'T':
        calculate()

    elif calc_again.upper() == 'N':
        print('Do zobaczenia!')
    else:
        again()
calculate()
again()
