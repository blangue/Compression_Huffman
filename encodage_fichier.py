#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Renan
#
# Created:     07/05/2020
# Copyright:   (c) Renan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""Template de l'encodage"""
"""Il n'existe pas de donner standard nous allons donc crée notre méthode d'encodage
Nous créons un header dit fix comprennant :
    2octets pour définir le nb d'octet du header
    1 octet pour définir la taille en octet des occurances et symbole codé avec 0 en plus a l'avant
    2 octet pour définir nb d'octet de data
    1 octet pour définir bit en trop
ensuite le header dix variable dépendant de notre liste avec alternance de caractère et de leur occurance nb octet non délimité

ensuite suite d'octet de data."""

import programe_décodage as pd
import création_arbreV3 as ca

#variable
headerHeader = 2
headerOccurance = 1
headerData = 2
headerBit = 1

def encoder(original_string, couples=0):
    #je vais crée un string de longueur n*8
    #j'enregistre le nombre de bit supplémentaire pour pouvoir les supprimers au décodage
    bit_supplement = 0
    while (len(original_string)%8)!=0 :
        bit_supplement +=1
        original_string = original_string + '0'
    # first split into 8-bit chunks
    bit_strings = [original_string[i:i + 8] for i in range(0, len(original_string), 8)]
    # then convert to integers
    byte_list = [int(b, 2) for b in bit_strings]

    #on récupere la taille des datas on la passe en binaire de la taille de la parti header data
    nb_octet_data = bin(len(byte_list))[2:]

    #on calcul le nb de 0 manquant pour faire le nb d octet nécéssaire que l'on rajoute a l'avant
    octet_data = list_octet(headerData,nb_octet_data)

    #enregistrement des bits supplémentaire a la fin des data
    nb_bit = bin(bit_supplement)[2:]
    octet_bit = list_octet(headerBit, nb_bit)


    #détermination de l'occurance la plus grande pour définition du nb d'octet pour coder
    m = max(couples)
    m = int(len(bin(m[0])[2:])/8)+1
    s = max(couples , key=lambda colonnes: colonnes[1])
    s = len(bytearray(s[1], 'utf-8'))
    octet_occurance =[bin(m)[2:]]
    for i in range(5-len(bin(m)[2:])):
        octet_occurance[0] = '0' + octet_occurance[0]
    octet_occurance[0] = bin(s)[2:] + octet_occurance[0]
    for i in range(8-len(octet_occurance[0])):
        octet_occurance[0] = '0' + octet_occurance[0]
    octet_occurance = list_octet(headerOccurance, octet_occurance[0])

    #création des octet de taille de header
    nb_octet_header = headerBit+headerData+headerHeader+headerOccurance+\
    len(couples)*(m+s)
    nb_octet_header = bin(nb_octet_header)[2:]
    octet_header = list_octet(headerHeader, nb_octet_header)
    final_list_octet = octet_header + octet_occurance + octet_data + octet_bit
    with open('byte.bin', 'wb') as f:
        f.write(bytearray(final_list_octet))
        for i in couples :
        #création du header variable la liste de caractère et de leurs occurances
        #incrémentation au fur et a mesure pour éviter les bug du au caractère
            j = list_octet(m,bin(i[0])[2:])
            f.write(bytearray(j))
            texte = i[1]
            for j in range(s-len(bytearray(i[1],'utf-8'))):
                texte = '\x00' + texte
            f.write(bytearray(texte,'utf-8'))
        f.write(bytearray(byte_list))
    return True

#fonction permettant la mise en forme des octets
def list_octet(taille , chaine):
    for i in range(8*taille-len(chaine)):
        chaine = '0' + chaine
    liste_octet = [chaine[i:i + 8] for i in range(0, len(chaine), 8)]
    liste = [int(b, 2) for b in liste_octet]
    return liste

def decode_list_octet(taille , chaine):
    for i in range(8*taille-len(chaine)):
        chaine = '0' + chaine
    return chaine

def convert_octet(liste):
    number = ''
    for i in liste:
        number += decode_list_octet(1,bin(i)[2:])
    number = int(number, 2)
    return number

def convert_octet_str(liste):
    number = ''
    for i in liste:
        number += decode_list_octet(1,bin(i)[2:])
    return number

def decoder(fichier):
    with open (fichier, 'rb' ) as f:
        t = f.read()
    octets = list(t)
    #on traite chaque élément du header a taille définit
    tailleHeader = convert_octet(octets[:2])
    del octets[:2]
    x = bin(int(octets[0]))[2:]
    for i in range(8-len(x)):
        x = '0'+x
    sym = x[:3]
    oc = x[3:]
    tailleSymbole =int(sym,2)
    tailleOccurance =int(oc,2)
    del octets[0]
    tailleData = convert_octet(octets[:2])
    del octets[:2]
    x=[]
    x = octets[:1]
    tailleBit = convert_octet(x)
    del octets[0]
    dict = octets[:(tailleHeader-6)]
    #on récupere la liste de couple simbole occurrence
    couples = []
    for i in range(6,len(t)-tailleData,tailleOccurance+tailleSymbole) :
        oc=t[i:i+tailleOccurance]
        oc = list(oc)
        oc = convert_octet_str(oc)
        nul = 0
        sym_nul = 0
        for j in range(tailleSymbole) :
            if t[i+tailleOccurance+j] == 0:
                sym_nul +=1
        tp = (int(oc,2),t[i+tailleOccurance+sym_nul:i+tailleOccurance+tailleSymbole].decode('utf-8'))
        couples.append(tp)
    del octets[:tailleHeader-6]
    #on crée notre suite binaire
    suitebinaire =''
    for i in octets:
        suitebinaire += decode_list_octet(1,bin(i)[2:])
    suitebinaire = suitebinaire[:-tailleBit]
    #on transforme notre liste de couple grace a l arbre
    couples = ca.code(couples)
    #on décrypte notre suite binaire
    decrypte = pd.decodage(couples,suitebinaire)
    return(decrypte)
