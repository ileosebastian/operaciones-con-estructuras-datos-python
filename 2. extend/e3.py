def word_backwards(word):
    letters = list()
    letters.extend(word)

    letters = ''.join(
        [l for l in reversed(letters)]
    )
    
    return letters

if __name__ == '__main__':
    word = input("Ingrese una cadena de texto: ") 

    word = word_backwards(word)

    print("\nDicha cadena, al reves, seria:" + "\n\t" + word)