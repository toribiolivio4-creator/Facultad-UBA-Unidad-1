#Cuento de la Pipa

while True:
    cuento = input("Te cuento el cuento de la buena pipa? si/no  ").lower()
    if cuento == "si":
        frase = input("Ingrese una frase: ")
        print(f"Yo no te pregunté {frase}, yo te pregunté si queres que te cuente el cuento de la buena pipa")
        break
    else:
        print("Está bien, no te cuento nada.")
        break