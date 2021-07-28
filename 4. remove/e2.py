
def print_matrix(matrix):
    for rows in matrix:
        for number in rows:
            print(number, end='  ')
        print()
    
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print("Matriz:")
print_matrix(matrix)

number = 0
flag = True
while flag:
    number = int(input("Elimine un numero de la matriz: "))
    for rows in matrix:
        if number in rows:
            flag = False 

for rows in matrix:
    if number in rows:
        rows.remove(number)
        
print("\nNueva matriz:")
print_matrix(matrix)