import random
# demander à l'utilisateur de saisir la longueur du mdp
longpass=int(input('donner la longueur du mot de passe'))
#la liste des lettres majuscules, min, nb, ponctuation
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~"
#regrouper les caracteres selectiones aleatoirement en un seul mot
password="".join(random.sample(s,longpass))

print(password)