from random import randint

# lista a trabajar:
numbers = [
    randint(1,101) for n in range(1000)
]


# ---- EJERCICIO 1:
print("\n--------- EJERCICIO 1: ---------")

print(numbers)
n = int(
    input("\nIngrese el numero del cual quiere saber la cantidad exitente: ")
)
counter = numbers.count(n)
if counter > 0:
    print("\tSi existe dentro de la lista!, y se repite ",counter)
else:
    print("No existe dentro de la lista.")

# ---- EJERCICIO 2:
print("\n--------- EJERCICIO 2: ---------")

def count_chars(str_):
    max_ = 0
    character = ''
    for char in str_:
        if str_.count(char) > max_:
            max_ = str_.count(char)
            character = char
    return character
    

l_str = list(input("\nIngrese una cadena de caracteres: "))

l_str.extend(l_str.pop())

print("El caracter que mas se repite es: ", count_chars(l_str))

# ---- EJERCICIO 3:
print("\n--------- EJERCICIO 3: ---------")

animals = [
    'murcielago', 'aguila', 'pez globo',
    'mono', 'Aguila', 'pez salmon',
    'pez Globo', 'mono', 'perro', 'perro',
    'lobo', 'murcielago', 'Gato', 'perro'
]

print("Lista de animales en un zoologico:")
for animal in animals:
    print("\t" + animal.title())

count_of_animals = dict(
    (animal.title(), animals.count(animal)) for animal in set(animals)
)

print("Cantidad de animales en el zoologico:")
print(count_of_animals)