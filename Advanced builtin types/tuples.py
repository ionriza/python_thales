# Initializarea tuplurilor
t = ()
print(f"Am initializat tupla fara elemente {t=}")
print(f"{t=} {type(t)=}")
t = (1)
print(f"Folosind parantezele rotunde cu un singur element, fara virgula, nu va crea o tupla")
print(f"{t=} {type(t)=}")
t = 1,
# sau
t = (1,)
print(t)
print(f"Folosind functia tuple")
t = tuple()
print(f"Am initializat o tupla fara elemente: {t}, {type(t)}")
t = tuple([1,2,3,4])
print(f"{t=} {type(t)=}")

# Acceswarea elementelor tuplului
print('primul element', t[0])
print('ultimul element', t[-1])
print('primele 2 elemente', t[0:2])

# Proprietatea de imutabilitate
try:
    t[0] = 5
except TypeError:
    print(f'Orice incercare de a modifica un element al tuplului, va rezulta intr-o exceptie '
          f'de tip TypeError')

# Hash-ul este facut pe baza ID-urilor elementelor
# care vor ramane la fel pe tot lifetime-ul obiectului,
# chit ca adaugam noi elemente in lista

t = ([], 'Dinamo', 'FCSB')
t[0].append('CFR')
print(t)

# immutable objects can be hashable,
# mutable objects can't be hashable

# An object is hashable if it has a hash value which never changes
# during its liftime

# Objects with the same value always have the same hash

# All the keys in a dictionary are immutable, hashable objects

# Only hashable objects can be used as keys in a dictionary
# Only hashable objects can be used as items in a set

# Hashes will never change during the object's lifetime


"""
Aceste functii vor arunca exceptia TypeError
t.sort()
t.reverse()
del t[0]
"""

# Dimensiunea tuplului
print(f'Tuplul {t} are {len(t)} elemente')
print(t.__len__())

# Concatenare
print('La fel ca si la liste, nu modificam tuplul, ci construim un tuplu nou')
print(t + ('Mioveni', 'Chindia'))

# Repetare
print('Operatorul de inmultire concateneaza tuplul cu el insusi de 3 ori')
print(t*3)

# Slicing
print('primele 2 elemente', t[0:2])

# Membership
print(f"Se afla Dinamo in tuplu? {'Da' if 'Dinamo' in t else 'Nu'}")

# index
print(f"{t.index('Dinamo')=}")

# count
t *= 3
print(f"{t.count('Dinamo')=}")
print(t)

# len
print(f"{len(t)=}")

t = (1,15,22,5)
print(f"{min(t)=}, {max(t)=}")