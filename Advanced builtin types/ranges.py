# Initializarea range-ului
r = range(10)
print(f'Numerele de la 0 inclusiv la 10 exclusiv: {list(r)}')
r = range(5,10)
print(f'Numerele de la 5 inclusiv la 10 exclusiv: {list(r)}')
r = range(1,10,2)
print(f'Numerele de la 1 inclusiv pana la 10 exclusiv, '
      f'din 2 in 2 {list(r)}')
r = range(10, 1)
print('Numarul de inceput este deja mai mare decat numarul de final'
      'deci lista este goala')
print(r)
r = range(10, 0, -1)
print('Daca folosim pasul negativ, putem genera numere in ordine descrescatoare')
print(list(r))

# Folosirea unui range

# Parcurgerea unei liste cu ajutorul index-ului rezultat
# din urma crearii obiectului de tip range
lista = ['hello', 1, 1.5, (45.5, 25.7), [0]]

for index in range(len(lista)):
    print(lista[index])

# Executarea unei instructiuni de N ori folosind range
# si throwaway variable
for _ in range(10):
    print('Python is awesome')

# in / not in
# slicing
# index
# count