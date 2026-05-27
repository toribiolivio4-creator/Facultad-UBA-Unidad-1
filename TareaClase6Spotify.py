#Spotify
canciones = ["Amor de Vago",
"Parte & Choke",
"Olvidarte",
"Si Antes Te Hubiera Conocido",
"Alegría",
"BAILE INoLVIDABLE",
"DEGENERE",
"Piel",
"DtMF",
"Luck Ra: Bzrp Music Sessions, Vol. 61",
"FASHONISTA",
"El Mundo es Tuyo",
"LUNA",
"Die With A Smile",
"Perdonarte, ¿Para Qué?",
"Conmigo Te Gustó",
"Beautiful Things",
"Lose Control",
"El Doctorado",
"Me Gusta",
"Cosa Linda",
"Nunca Lo Olvides",
"Tan Solo",
"Esta Saliendo El Sol",
"Amanece",
"SINVERGÜENZA",
"Un Besito Más",
"Es un Secreto",
"No Se Va",
"LA CANCIÓN",
"111",
"Creo",
"El Amanecer",
"EL DÍA DEL AMIGO",
"Te Quería Ver",
"Comernos",
"En Otra Vida - Versión Cuarteto",
"Bicho de Ciudad",
"Yo Era",
"A Ti",
"M.A.I",
"Princesa",
"Puesto",
"Loca",
"Rara Vez",
"Encantadora",
"Te Vas a Arrepentir",
"UN SIGLO SIN TI",
"Tu Foto",
"Un Ángel para Tu Soledad"]


for i in canciones:
    diez_primeros = canciones[:9]
    print(diez_primeros)

    tres_primeros = canciones[:3]
    tres_ultimos = canciones[47:]
    print(tres_primeros)
    print(tres_ultimos)

    cancion_favorita = canciones[1] = "Message in a Bottle"
    print(cancion_favorita)
    
    if "Perfecta" not in canciones:
        print("Perfecta no está en la lista")
    else:
        print("Perfecta está en la lista")  