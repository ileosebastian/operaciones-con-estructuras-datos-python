
numbers = [x for x in range(1, 101)]

def print_numbers(li):
    i = 0
    for n in numbers:
        print(n, end='  ')
        i = i+1
        if i % 10 == 0:
            print()

print("Todos los numeros")
print_numbers(numbers)

decision = int(input("¿Desea eliminar numeros impares (1) o pares (0): "))

if decision:
    for n in numbers:
        if n % 2 != 0:
            numbers.remove(n)
else:
    for n in numbers:
        if n % 2 == 0:
            numbers.remove(n)
    
print("\nNuevo conjunto de numeros")
print_numbers(numbers)