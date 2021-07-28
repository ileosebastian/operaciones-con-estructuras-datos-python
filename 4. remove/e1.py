
people = [
    "Lego",
    "Carlina",
    "Hugo",
    "Patata",
    "Xavier"
]

print("La lista de personas es:")
for person in people:
    print(person)

people.remove("Patata") # ELIMINAR a aquel que no es una persona

print("\nLa lista limpia es:")
for person in people:
    print(person)