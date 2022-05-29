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

##programme arbre


class noeud:
    ##création d'un noeud qui permettra de crée des liens entre chaque niveau
    ## data est de la forme d'une liste tel que [(45,A),(20,B)]
    ## liste de tuples avec en premier le nb d'occurance en deuxième la lettre

    def __init__(self,key = 0 , data = None):
        self.code= None
        self.data = data
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def add_data(self,data):
        self.left = data[0]
        self.right = data[1]
        self.left.actualisation_code(0)
        self.right.actualisation_code(1)


    def actualisation_code(self, position):
        if self.code == None:
            self.code = str(position)
        else:
            self.code = str(position)+self.code
        if(self.left != None):
            self.left.actualisation_code(position)
        if(self.right != None):
            self.right.actualisation_code(position)

    def code_feuilles(self):
        codes=[]
        if(self.left != None):
            codes.extend(self.left.code_feuilles())
        else:
            return(self.data,self.code)
        if(self.right != None):
            codes.extend(self.right.code_feuilles())
        else:
            return(self.data,self.code)
        return codes

    def feuille(self, data):
        code=[]
        if self.left != None and self.left.data == data :
            return(self.left.code, self.left.data)
        elif(self.left != None):
            test = self.left.feuille(data)
            if test != [] :
                code= test
        if self.right != None and self.right.data == data :
            return(self.right.code, self.right.data)
        elif(self.right != None):
            test = self.right.feuille(data)
            if test != [] :
                code = test
        return code


    def destroy(self):
        if(self.left.left != None and self.left.right != None):
            self.left.destroy()
        else:
            del self.left
        if(self.right.left != None and self.right.right != None):
            self.right.destroy()
        else:
            del self.right


#une fonction qui retourne les couples code symbole
def code(occurances):
    for i in range(len(occurances)):
        occurances[i] = noeud(occurances[i][0], occurances[i][1])
    while(len(occurances)>1):
        i=0
        newKey = occurances[0].key +  occurances[1].key
        data = occurances[0:2]
        del occurances [0:2]
        while(i< len(occurances) and newKey > occurances[i].key ):
            i+=1
        occurances.insert(i,noeud(newKey))
        occurances[i].add_data( data[0:2])
    codes = occurances[0].code_feuilles()
    #on remet cette liste sous forme de tuple plus simple à lire
    couples=[]
    for i in range(0,len(codes),2):
        couples.append((codes[i+1],codes[i]))
    return couples

#une fonction qui retourne juste l'arbre
def arbre(occurances):
    for i in range(len(occurances)):
        occurances[i] = noeud(occurances[i][0], occurances[i][1])
    while(len(occurances)>1):
        i=0
        newKey = occurances[0].key +  occurances[1].key
        data = occurances[0:2]
        del occurances [0:2]
        while(i< len(occurances) and newKey > occurances[i].key ):
            i+=1
        occurances.insert(i,noeud(newKey))
        occurances[i].add_data( data[0:2])
    return occurances #liste contenant juste le noeud root de l'arbre


#code néscessaire pour l'utilisation de la classe laisser en exemple ici
""" programme exemple d'utilisation de la classe noeud
#on entre une liste
liste=[(25,'A'),(12,'B'),(10,'C'),(7,'D'),(48,'E'),(5,'F'),(15,'L')]

"""