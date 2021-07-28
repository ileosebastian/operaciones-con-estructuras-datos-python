
vectors = [
    (0,0, ''),
    (3,1, 'derecha'),
    (0,-25, 'derecha'),
]

if __name__ == '__main__':
    
    print("Conjunto de vectores: ")
    print(vectors)
    message = """
        Ingrese un vector con con coordadas x e y, 
        y su direccion (izquierda o derecha).
    """
    print(message)

    new_vector = (
        int(input("Coordenada x: ")),
        int(input("Coordenada y: ")),
        input('Direccion (izquieda o derecha): ')
    )

    vectors.insert(1,new_vector)

    print("\nNuevo conjunto de vectores: ")
    print(vectors)
    
    