# Initializarea seturilor
s = {}
print(f'{s=} este {type(s).__name__}')
s = set()
print(f'{s=} este {type(s).__name__}')
s = {1, 2, 3}
print(f'{s=} este {type(s).__name__}')
s = {1, 2, 2, 3, 4, 4}
print(f'Desi am specificat duplicate, odata initializat, setul s '
      f'va contine elemente unice')
print(s)
s = set([1, 2, 2, 3, 4, 4])
print(f'{s=} este initializat folosind functia set')
s = {x for x in [1, 2, 2, 3, 4, 4]}
print(f'{s=} este initializat folosind set comprehension')

# Operatii de modificare
s = {1, 2, 3}
s.add(4)
print(f'Folosim metoda add pentru a adauga')
print(s)
print(f'Folosim metoda remove pt a sterge')
s.remove(3)
print(f'Am scos 3 si a ramas {s}')
try:
    s.remove(5)
except KeyError:
    print('Exceptie')
s.discard(5)
elem = s.pop()
print(f'Elementul scos arbitrar din set este: {elem}')
print(s)
print(f'Actualizam setul cu inca 3 numere')
s.update((5, 6, 7))
print(s)
print(f'Stergem toate elementele folosind clear')
s.clear()

try:
    del s[0]
except TypeError as e:
    print(str(e))

# Operatii cu multimi

a = {1, 2, 3}
b = {3, 4, 5}
print('Reuniunea sau union')
print(a.union(b))
print(a | b)
print('Intersectia sau interesction')
print(a.intersection(b))
print(a & b)
print('Diferenta sau difference')
print(a.difference(b))
print(a - b)

# membership
print(f'1 se afla in set? {1 in a}')
print(f'5 nu se afla in set? {5 not in a}')

# len
print(f'Lungimea setului este de {len(a)} elemente')