
matrix = []

for i in range(1, 5):
    rows = []
    for j in range(1, 5):
        rows.append(
            int(input("Fila {0} Columna {1}: ".format((i),(j)))) 
        )
    print("\nListo!\n")
    matrix.append(list(rows))

print("Matriz resultante")
for rows in matrix:
    for number in rows:
        print(number, end=' ')  
    print()