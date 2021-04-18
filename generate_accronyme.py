
texte=str(input('donner une chaine de caractere: '))

def accro_gen(chaine):
    mots = chaine.split()
    accro = ''
    for i in mots:
        accro = accro + str(i[0]).upper()
    return accro

resulat=accro_gen(texte)

print(f"voici l'accronyme {resulat}")