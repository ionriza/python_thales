# Initializarea dictionarelor
d = {}
print(f"{d=} {type(d)=}")
d = dict()
print(f"{d=} {type(d)=}")
d = {"Python": 5, "C": 1, "C++": 2}
print(f"{d=} {type(d)=}")
print(f'Putem construi un dictionar folosind un iterabil')
# Fiecare element in iterabil trebuie sa fie si el un interabil
# care sa contina 2 obiecte
d = dict([('Python', 5), ('C', 2), ('C++', 3)])
print(f"{d=} {type(d)=}")
# Pentru a obtine un astfel de iterabil, putem folosi functia zip
# care primeste un numar de iterabile si intoarce un obiect de tip
# zip, care poate fi interpretat ca o lista cu tuple ce contin
# elemente doua cate doua, luate pozitional
d = dict(zip(['Python', 'C', 'C++'], [5, 2, 3]))
print(f"{d=} {type(d)=}")
print(f'Putem construi un dictionar cu un alt dictionar (mapping)')
d = dict({'Python': 5, 'C': 2, 'C++': 3})
print(f"{d=} {type(d)=}")
print(f'Putem construi un dictionar cu argumente keyword')
d = dict(Python=5, C=2, cpp=3)
print(f"{d=} {type(d)=}")
print(f'Putem construi un dictionar cu dict comprehension')
d = {k: v for k, v in [('Python', 5), ('C', 2), ('C++', 3)]}
print(f"{d=} {type(d)=}")
print(f'Cu ajutorul dict comprehension putem inlocui cheie-valoare')
# d = {v: k for k, v in [('Python', 5), ('C', 2), ('C++', 3)]}
# print(f"{d=} {type(d)=}")

# Accesarea elementelor
print(f"{d['Python']=}")
try:
    print(d['C#'])
except KeyError:
    print('Arunca o eroare de tip KeyError pentru ca cheia'
          ' C# nu exista in dictionarul d')
print(d.get('C#'))
v = d.get('C#', 'No language')
print(f'Daca nu exista chiea C#, imi  va intoarce {v}')



