def trier(fichier):
    #Creation des deux liste
    liste=[]
    liste_total=[]
    with open (fichier,encoding='utf-8',mode='r') as f:
        #Etape 1 : trier sous forme de liste
        for ligne in f:
            for car in ligne:
                #Pour la premiere lettre/occurance quand liste vide
                if len(liste)==0:
                    liste.append(1)
                    liste.append(str(car))
                else:
                    #Ensuite on test si le caractere est présent dans la liste
                    trouvé=False
                    for i in range (len(liste)):
                        if (i%2)!=0: #Les lettres sont présents que sur les impairs
                            if liste[i]==car:
                                trouvé=True
                                place=i
                    #Si il est présent on incrémente
                    if trouvé==True:
                        liste[place-1]+=1
                    #Si il est pas présent on ajoute
                    elif trouvé==False:
                        liste.append(1)
                        liste.append(str(car))
    for j in range (len(liste)-1):
        #Mets la liste sous forme de tuple
        if (j%2)==0:
            liste_total.append((liste[j],liste[j+1]))
    return liste_total