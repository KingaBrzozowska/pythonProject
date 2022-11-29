slownik1 = {"1":1}
slownik2 = {"2":2}
slownik3 = {}
print(slownik1)
slownik1 |= slownik2
slownik3 |= slownik1

print(slownik1)
print(slownik3)


#print(slownik1 | slownik2) # łaczenie slownikow, ostatni (z prawej) jest licozny jesli sie powtarza

a = {'a': 1}
b = {'a': 3, 'b': 2}
print({**a, **b})
