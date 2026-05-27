#Cuento

while True:
    pregunta = input("Querés que te cuente un cuento? si / no   ").lower()
    if pregunta == "si":
        frase_usuario = input("Ingrese una frase:  ")
        print(f"Yo no te dije: {frase_usuario}, yo te pregunté si querías que te contara el cuento de la buena pipa.")
        break
    elif pregunta == "no":
        print("Está bien, no te cuento nada... jodete")
        break
    else:
        print("Fijate porque en vez de poner Si o No, pusiste cualquier verdura!!")
        break