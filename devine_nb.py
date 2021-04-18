import random
nombre_choisi=random.randint(1,6)
resultat=0

for i in range(3):
    nombre_propose = int(input('saisir un nombre: '))
    if nombre_propose==nombre_choisi:
        resultat=1
        break
    elif nombre_propose > nombre_choisi:
        print("Le nombre que vous avez proposé est supérieur à celui que j'ai choisi")
    elif nombre_propose < nombre_choisi:
        print("Le nombre que vous avez proposé est inferieur à celui que j'ai choisi")

if resultat==1:
    print("bravo, bien joué")
    print(f"le bon numero est {nombre_choisi}")
else:
    print(f'vous perdez, le bon numero etait {nombre_choisi}')