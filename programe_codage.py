def codage (texte,lettres):
    ## lettres est de type Liste de tuple tel
    ## que lettres=[(A,001),(F,000),(C,01)]
    texte=list(texte)
    code=''
    for i in texte:
        j=0
        while j < len(lettres) and i != lettres[j][1] :
            j+=1
        if j >= len(lettres):
            return False
        else :
            code += lettres[j][0]
    return code ## code aura la forme '01001000'

"""
liste = [('01','C'),('000','F'),('001','A')]
texte = 'CAFT'
print(codage(texte,liste))"""
