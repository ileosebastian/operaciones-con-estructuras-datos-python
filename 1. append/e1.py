
# lista de animales:
animals = ["leon", "cocodrilo", "Venado", "vaca"]

flag = True
while flag:
    animals.append(
        input("Ingrese el nombre de un animal: ").lower()
    )
    flag = True if input("\t¿Desea igresar otro? (s/n): ").lower() == 's' else False
   
print("\nLos animales de la lista son:")
for animal in animals:
    print(animal.title()) 