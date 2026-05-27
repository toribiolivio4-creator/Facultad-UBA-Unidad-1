#Facu
print("Si está soledado me meto a la pileta, si está ventoso me meto igual  y si está lluvioso no me meto.")

clima = str(input("Como está el clima? (soleado / ventoso / lluvioso)")).lower()

if clima == "soleado":
    print("Me meto")
elif clima == "ventoso":
    print("Me meto")
elif clima == "lluvioso":
    print("No me meto")  
else:
    print("Dato no encontrado")          