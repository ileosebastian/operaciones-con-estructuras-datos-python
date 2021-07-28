
stack_of_strings = [
    "Leo",
    "Carlina",
    "Miguel",
    12.4,
    "Jose",
    "Milena",
    False
]

print("Ingreso de elementos a la pila usando append.")

stack_of_strings.append( # ingreso de un entero
    int(input("Ingrese un numero entero: "))
)
stack_of_strings.append( # ingreso de un float
    float(input("Ingrese un numero con comas (.): "))
)
stack_of_strings.append( # ingreso de un booleano 
    bool(input("Ingrese un valor binario (0 o 1): "))
)

print("\nLa pila de elementos es la siguiente:")
print(stack_of_strings)