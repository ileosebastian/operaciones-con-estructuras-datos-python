
class Routine:
    def __init__(self, name_routine):
        self.__name = name_routine
        
    def deploy_routine(self, id):
        print("Routine {0}: '".format(id) + self.__name + "' is running!")

routines = []

if __name__ == '__main__':
    routine_1 = Routine('Analizar cadena de texto')
    routine_2 = Routine('Ordenar datos')
    routine_3 = Routine('Insertar nuevos registros a una Base de Datos')

    routines.append(routine_1)
    routines.append(routine_2)
    routines.append(routine_3)

    i = 1
    for routine in routines:
        routine.deploy_routine(i)
        i = i+1
    
    while True:    
        print("Ingrese otra rutina entre las que ya estan hechas.")
        index = int(input("\tRoutine ID: "))
        if index not in range(1, len(routines)+1):
            continue
        else:
            name_routine = input("\tNombre de la rutina: ")
            break

    routines.insert(index-1, Routine(name_routine))

    print("\nNueva lista de rutinas.")
    i = 1
    for routine in routines:
        routine.deploy_routine(i)
        i = i+1
