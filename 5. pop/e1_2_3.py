
def print_stack(stack, message='\n'):
    print(message)
    for element in stack:
        print(element, end='  ')

# estructura a trabajar
stack_a = ['A', 'B', 'C']
stack_b = []
stack_c = []

# ---- EJERCICIO 1:
print("\n--------- EJERCICIO 1: ---------")
print_stack(stack_a, '\nPila A')

# introducir el ultimo elemento de la pila A en B
stack_b.append(stack_a.pop())

stack_b.append(stack_a.pop())

print_stack(stack_b, '\nPila B')
print_stack(stack_a, '\nPila A')

stack_c.append(stack_b.pop(0)) # sacar el primer elemento en vez del ultimo
print_stack(stack_c, '\nPila C')

# ---- EJERCICIO 2:
print("\n--------- EJERCICIO 2: ---------")
# algoritmo de torre de hanoi
def hanoi(n, P1, P2, P3):
    if n == 0:
        # No hay mas discos a mover en este paso
        return
    global count # contador global
    count += 1
    # mover n-1 discos desde P1 a P2
    hanoi(n-1, P1, P3, P2)
    if P1:
        # mover el dicto desde P1 a P3
        P3.append(P1.pop())
        print(A, B, C)
    # mover n-1 discos desde P2 a P3
    hanoi(n-1, P2, P1, P3)

# Inicializar las pilas: todos los n discos están en el polo A. 
n = 4
A = list(range(n,0,-1))
B, C = [], []

print(A, B, C)
count = 0
hanoi(n, A, B, C)
print("Pasos:", (count+1))


# ---- EJERCICIO 3:
print("\n--------- EJERCICIO 3: ---------")
books = []
def print_books(books): # apila y desapila libros
    tmp = []
    print("La pila de libros queda asi:")
    while len(books) > 0:
        b = books.pop() # uso de pop()
        print("\t" + b)
        tmp.append(b)
    return  tmp
    
        
print("La lista de libros a leer esta vacia.")
flag = True
while flag:
    book = input("Ingrese un libro: ")
    books.append(book)
    books = print_books(books) 
    
    decision = input("¿Desea ingresar otro? (s/n): ")
    flag = True if decision.lower() == 's' else False

print()
books = print_books(books) 
