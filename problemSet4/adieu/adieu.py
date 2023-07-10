import inflect

p = inflect.engine()

coleccion = []
while True:
    try:
        word = input("Name: ")
        coleccion.append(word)
    except EOFError:
        print()
        break


goodbye = p.join(coleccion)
print("Adieu, adieu, to", goodbye)
