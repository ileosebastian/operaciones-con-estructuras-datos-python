
# lenguas germanicas
germanic_languages = [
    "Ingles", 
    "Aleman", 
    "Noruego", 
    "danes", 
    "sueco"
]

# lenguas romances
romance_languages = [
    "Español", 
    "Frances", 
    "Italiano", 
    "Portugues"
]

all_languages = [] # unificacion de todos los lenguajes
all_languages.extend(germanic_languages)
all_languages.extend(romance_languages)

print("Conjunto de todas las lenguas del mundo:")
print(all_languages)

# nuevo conjunto de idiomas!
# lenguas asiaticas
asian_languages = ["Chino", "Coreano", "Japones"]

all_languages.extend(asian_languages)

print("\nNuevo conjunto de todas las lenguas del mundo:")
print(all_languages)