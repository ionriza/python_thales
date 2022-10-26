# Initializarea string-ului
s = 'hello world'
s = "hello world"
s = '''hello world'''
# ghilimelele triple pot fi folosite pentru a crea docstringuri
# Docstring-urile sunt stringuri care apar in definirea functiei, metodei, clasei sau modulului
s = '''hello
world'''
s = 'hello' 'world'
# Daca nu avem niciun obiect dat functiei str, o sa intoarca un string gol
str_obj = str()
str_obj = str(1)

# Afisarea stringului
print(s)

# Verificarea tipului variabilei
print(type(s))

# Verificarea listei cu atribute si metode ale obiectului s
# In Python, orice este un obiect
print(dir(s))

# Accesarea caracterelor stringului cu ajutorul index-ului
# Indexarea incepe de la stanga la dreapta, de la 0 la N-1, unde N este lungimea stringului
print('Primul caracter', s[0])
print('Al doilea caracter', s[1])
print('Ultimul caracter', s[-1])
print('Penultimul caracter', s[-2])

# String slicing
print('extragem caracterele pornind de la cracterul 1 inclusiv pana la caracterul 3 exclusiv')
print(s[1:3])
print('extragem carcaterele pornind de la caracterul 1 inclusiv pana la final')
print(s[1:])
print('extragem caracterele pornind de la inceput pana la caracterul 3 exclusiv')
print(s[:3])
print('extragem caracterele pornind de la caracterul 1 inclusiv pana la 6 exclusiv, din 2 in 2')
print(s[0:6:2])
print('extragem caracterele pornind de la caracterul 13 pana la 16 pt a observa ca '
      'operatia de string slicing este handled graceful')
print(s[13:16])
print('extragem caracterele in ordine inversa')
print(s[::-1])
print('intoarce o copie a sirului')
print(s[:])

# Accesarea caracterelor unui string cu un index mai mare, va arunca o eroare de tip
# IndexError
try:
    print(s[15])
except IndexError:
    print('Am prins un IndexError')

# Proprietatea de imutabilitate
try:
    s[1] = 'p'
except TypeError as e:
    print('!'*16+str(e))
# s = 'New Hello world'
# Nu modificam continutul lui s, ci il suprascriem complet

# Lungimea unui sir
print(f'Stringul s are {len(s)} caractere')
print(f'Stringul s are {s.__len__()} caractere')

# Accesarea ultimului element dintr-un sir cu ajutorul functiei len
print(s[len(s)-1])
print(s[-len(s)]) # primul element cu index negativ

# Operatii specifice secventelor

# 1.Concatenarea
print('Hello' ' ' 'world')
print('Hello' + 'world')
s = 'hello'
t = 'world'
print(s+t)

# 2. Repetarea
print(s*3)
print('hello'*3)

# 3. Operatia de apartenenta (membership)
print('Litera h este in string-ul s?', 'h' in s)
print('Merge si sa cautam substring ll in string hello?', 'll' in s)
print('Litera f este in string-ul s?', 'f' in s)
print('Litera f nu este in string-ul s?', 'f' not in s)

# 4. Index-ul caracterului
# Index-ul primei ocurente a substringului 'ell' in string-ul s.
print(f"Index-ul substringului ell din string-ul {s} este {s.index('ell')}")
print(f"Index-ul substring-ului lo din string-ul {s} incepand cu index-ul 1 este {s.index('lo', 1)}")
# Accesarea unui index unui string/substring care nu exista,
# va arunca o eroare de tip ValueError: substring not found
try:
    print(s.index('ff'))
except ValueError:
    print('Am prins o eroare de tip ValuError')

# 5. Count
# Numarul total de ocurente a string-ului dat ca argument in string-ul s
print(f"Gasim litera l de {s.count('l')} ori")

# Parcurgerea unui string
print('Parcurgere directa')
for elem in s:
    print(elem)
print('Parcurgerea cu range')
for i in range(len(s)):
    print(s[i])
print('Parcurgerea cu enumerate')
for i, element in enumerate(s):
    print(i, element)
print('Parcurgerea inversa')
for i in range(len(s)-1, -1, -1):
    print(s[i])
for elem in s[::-1]:
    print(elem)

# Compararea stringurilor
print('Este caracterul a mai mare decat b?', 'a' > 'b')
print(f"Valorea ASCII numerica a caracterului a este {ord('a')}")
print(f"Valorea ASCII numerica a caracterului a este {ord('b')}")


# Metode specifice string-urilor
print(f'String-ul s cu litere mari: {s.upper()}')
print(f'String-ul s cu litere mici: {s.lower()}')
print(f'String-ul s cu cu majuscula: {s.capitalize()}')
print(f"Verificarea string-ului daca incepe cu litera h: {s.startswith('h')}")
print(f"{s} {'incepe' if s.startswith('g') else 'nu incepe'} cu litera g")
print(f"String-ul {s} se termina"
      f" cu o vocala?: {s.endswith(('a','e','i','o','u'))}")
print(f"Index-ul substring-ului h este {s.find('el')}")
print(s.find('g'))
print(f"Inlocuim litera l cu c: {s.replace('l','c')}")
print(f"Inlocuim doar prima litera l cu c: {s.replace('l','c', 1)}")
s = 'I like Python'
print("Impartim string-ul cu ajutorul metodei split")
s_splited = s.split()
print("Daca nu dam niciun argument metodei split, acesta va separa string-ul"
      "dupa spatiile libere")
print(s_splited, type(s_splited))
# Putem face si method chaining
print(s.replace(' ', '-').split('-'))
print(f'A rezultat o lista cu {len(s_splited)} elemente de tip {[type(x) for x in s_splited]}')
print('Inlocuim spatiile libere cu linii ')
s = s.replace(' ', '-')
print(s)
print('Si separam dupa linii')
print(s.split('-'))
s = '  Hello World    '
# In Python 3.8, putem debuga mai usor in f-string-uri, adaugand egalul (=) la finalul expresiei
# acesta va afisa atat expresia cat si valoarea
print(f"{s=} va fi dupa strip: {s.strip()=}")
print(f"{s=} va fi dupa rstrip: {s.rstrip()=}")
print(f"{s=} va fi dupa strip: {s.lstrip()=}")
s = 'helloworld\n'
print(s)
print(f"{s=} va fi dupa strip: {s.strip()=}")