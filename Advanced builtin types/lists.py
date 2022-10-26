# Initializarea listelor
lista = []
print(f'Am initializat o lista fara elemente: {lista}')
print(f'Verificam tipul listei', {type(lista)})
lista = [1, 1.5, True, 'hello', [1, 2, 3], {'key': 'value'}, {1, 2, 3}, None, range(5)]
print(f"Am initializat o lista cu elemente de tip diferit: {lista}")
for elem in lista:
    print(elem, type(elem))
lista = [i for i in 'hello']
print(f"Am initializat o lista prin list comprehension: {lista}")
lista = list()
print(f"Am initializat o lista fara elemente cu ajutorul functiei list: {lista}")
lista = list('hello')
print(f"Am initializat o lista cu un iterabil cu ajutorul functiei list: {lista}")

# Accesarea elementelor
print(f"Accesarea primului element {lista[0]}")
print(f"Accesarea ultimului element {lista[-1]}")
print(f"Accesarea primelor doua elemente {lista[0:2]}")

# Variable unpacking (functioneaza cu orice iterabil, deci si la stringuri)
print(f"Folosind, atat list slicing, cat si intreaga lista, putem atribui variabile "
      f"elementelor listei, folosind conceptul de variable unpacking")
print(f"Cand lista nu e prea mare")
new_list = [1, 2, 3]
a, b, c = new_list
print(f"{a=}, {b=}, {c=}")
print(f"Cu ajutorul list slicing")
d, e = new_list[0:2]
print(f"{d=}, {e=}")

# Actualizarea elementelor

# DENUMESTE lista CA liga_1

lista = ['FCSB', 'CFR', 'Farul Constanta', 'Rapid Bucuresti']
print(f"Folosim lista {lista}")
print(f"Vom modifica primul al doilea element al listei")
scos = lista[1]
lista[1] = 'U Cluj'
print(f"A iesit {scos}, a intrat {lista[1]}")
print(f"Vom modifica ultimul element al listei, pentru a demonstra folosirea indexului negativ")
scos = lista[-1]
lista[-1] = 'Dinamo Bucuresti'
print(f"A iesit {scos}, a intrat {lista[-1]}")
print(f"Asa arata lista acum: {lista}")

# Pentru a actualiza mai multe elemente, putem folosi list slicing
# numai ca variabila trebuie sa fie un iterabil
print(f'Lista inainte de actualizare: {lista}')
lista[0:2] = ['Universitatea Craiova', 'FC Voluntari']
print(f'Lista dupa actualizarea primelor 2 elemente folosind list slicing: {lista}')

# Adaugarea elementor
print(f"Deloc ortodox, folosind list slicing")
lista[4:4] = ['FCSB']
print(f"Lista dupa adaugarea elementelui folosind list slicing {lista}")
print(f"Cu ajutorul metodei append")
lista.append('Petrolul Ploiesti')
print(f"Lista dupa metoda append {lista}")
lista.extend(['FC Botosani', 'CS Mioveni'])
print(f"Lista dupa metoda extend {lista}")
lista.insert(0, 'U Craiova')
print(f"Lista dupa inserarea U Craioviei inainte de primul element")
print(lista)
print(f"Folosind operatorul de adunare")
lista += ['FC Arges']
print(lista)

# Stergerea elementelor listei
print(f"Folosind metoda pop fara argument")
print(f"Pentru a nu retrograda ultima echipa adaugata manual, vom amesteca lista")

from random import shuffle, randint

shuffle(lista)
retrogradare = lista.pop()
print(f'Echipa retrogradata este {retrogradare}')
print(f"Asa arata lista dupa retrogradarea ultimei echipe din lista: {lista}")
index_retrograde = randint(0, len(lista)-1)
print(f"Vom retrograda echipa de la index-ul {index_retrograde}")
retrogradare = lista.pop(index_retrograde)
print(f"Echipa retrogadata este {retrogradare}")
print(lista)
print(f"Stergem ultimul element din lista cu metoda remove")
lista.remove(lista[-1])
print(f"Vom sterge primul element cu ajutorul cuvantului cheie del")
del lista[0]
print(f"Vom sterge toata lista cu metoda clear")
lista.clear()
print(f"Lista {lista} dupa stergerea elementelor")

# Alte metode
lista = ['FCSB', 'CFR', 'Farul Constanta', 'Rapid Bucuresti']
lista.sort()
# Sort ordoneaza lista crescator in-place si intoarce None
# Daca vrem sa ordoneze descrescator, avem parametrul reverse
print(f"Lista dupa sortare: {lista}")
lista.reverse()
print(f"Lista dupa operatia de reverse")
print(lista)

lista2 = lista.copy() # acelasi lucru cu lista2 = lista[:]
lista2[0] = 'CSM Valcea'
print(lista, lista2)

lista = [['Dinamo', 'Steaua'], 'FCSB']
lista2 = lista.copy()
lista[1] = 'Viitorul'
print(lista, lista2)
lista[0][0] = 'Slatina'
print(lista, lista2)
# Modificarea elementului lista[0][0] se va vedea si in lista2[0][0]

# Pe langa asta:
# # operatiile comune secventelor
# concatenare
# repetare
# membership
# slicing
# # functiile comune secventelor
# len
# min
# max
# count
# index
# # parcurgerea listelor
