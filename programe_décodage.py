def decodage(liste,suitebinaire):
    mot=''
    suitebinaire=list(suitebinaire)
    while len(suitebinaire) != 0 :
        r=0
        occurance=1
        while (r!=True):
            test=''
            for j in range(occurance):
                test+=suitebinaire[j]
            for i in range( len(liste) ):
                if liste[i][0]==test :
                    r=True
                    mot+=liste[i][1]
                    del suitebinaire[0:j+1]
                    break
            occurance +=1

    return(mot)

"""
liste=[('01','C'),('000','F'),('001','A')]
suitebinaire='01001000'
print(decodage(liste,suitebinaire))"""
