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
import encodage_fichier as ef

fichier_encode=str(input("Quelle est le nom de votre fichier encode? Ecrire : nomfichier"))
row = str(input("si vous souhaitez lire taper 1 si vous souhaitez décrypter taper 2"))

if row =='1':
    print(ef.decoder(fichier_encode))
elif row =='2':
    with open('fichier_décoder.txt',encoding='utf-8', mode ='w') as f :
        f.write(ef.decoder(fichier_encode))