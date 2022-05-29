#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Renan
#
# Created:     25/05/2020
# Copyright:   (c) Renan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import création_arbreV3 as ca
import occurence_symbole as os
import programe_codage as pc
import encodage_fichier as ef
import programe_décodage as pd



fichier=str(input("Quelle est le nom de votre fichier? Ecrire : nomfichier.txt"))
liste = os.trier(fichier)

# nous allons crée l'arbre

#on trie la liste car elle n'arrive pas forcément trié
occurances = [(ocurrance, lettre) for ocurrance,lettre in sorted\
                        (liste, key=lambda colonnes: colonnes[0])]

x = [0 for i in range(len(occurances))]
for i in range(len(occurances)):
    x[i]=occurances[i]
#codes est de la forme d'une liste ou alterne les symboles et les codes associés

couples = ca.code(occurances)

#on appelle pc.codage qui prend en arguement un text et les couples de tuples
#si le texte contient des symboles non codés alors return False
#texte de la forme str

texte=str(input("Quel texte souhaitez vous encoder?"))

#je test si le texte est un fichier ou non
try:
    with open(texte, encoding='utf-8', mode =
    'r') as fichier :
        texte = fichier.read()
except IOError:
    print('error')
texte_compresser = pc.codage(texte,couples)

if texte_compresser == False :
    print("erreur un symbole du texte n'a pas de code associé")
else:
    print(ef.encoder(texte_compresser,x))
