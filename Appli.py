import tkinter as tk
import tkinter.filedialog as tkf
import création_arbreV3 as ca
import occurence_symbole as os
import programe_codage as pc
import encodage_fichier as ef
import programe_décodage as pd

dim=50
class Application():

    def __init__(self,w=10,h=10):
        self.w=w
        self.h=h
        self.page=0
        self.fichier=''
        self.wnd = tk.Tk()
        self.wnd.title('Application')
        self.wnd.geometry("-0+0")
        self.cnv = tk.Canvas(self.wnd, width=dim*self.w, height=dim*self.h, bg='pink')
        self.cnv.pack(side=tk.LEFT)
        self.text = self.cnv.create_text(250,250,text="Z'est partiiiiii !",font=('Helvetica',50))
        self.quitte = tk.Button(self.wnd,text='Quitter',command=self.wnd.destroy)
        self.quitte.pack(side=(tk.RIGHT and tk.BOTTOM))
        self.b1 = tk.Button(self.wnd,text='Huffman',command=self.etapes)
        self.b2 = tk.Button(self.wnd,text='Bouton 2',command='None')
        self.b3 = tk.Button(self.wnd,text="Afficher l'arbre",command= self.afficher_arbre )
        self.b4 = tk.Button(self.wnd,text='Encoder',command=self.encoder)
        self.b5 = tk.Button(self.wnd,text='Décoder',command=self.decoder)
        self.b1.pack(side=(tk.RIGHT and tk.TOP),padx=5,pady=5)
        self.b2.pack(side=(tk.RIGHT and tk.TOP),padx=3,pady=5)
        self.b3.pack(side=(tk.RIGHT and tk.TOP),padx=5,pady=5)
        self.b4.pack(side=(tk.RIGHT and tk.TOP),padx=5,pady=5)
        self.b5.pack(side=(tk.RIGHT and tk.TOP),padx=5,pady=5)
        self.wnd.mainloop()

    def etapes(self):
        self.cnv.delete('all')
        if self.page==0:
            self.cnv.delete(self.text)
            self.cnv.create_rectangle(30,40,80,60)
            self.cnv.create_text(55,50,text='7',font=('Helvetica',15))
            self.cnv.create_rectangle(120,40,180,60)
            self.cnv.create_text(150,50,text='37',font=('Helvetica',15))
            self.cnv.create_rectangle(230,40,280,60)
            self.cnv.create_text(255,50,text='12',font=('Helvetica',15))
            self.cnv.create_rectangle(320,40,380,60)
            self.cnv.create_text(350,50,text='56',font=('Helvetica',15))
            self.cnv.create_rectangle(430,40,480,60)
            self.cnv.create_text(455,50,text='8',font=('Helvetica',15))
            self.titre = self.cnv.create_text(250,120,text='Etape 1: mise en ordre croissant',font=('Helvetica', 20))
            self.fleche = self.cnv.create_line (250, 150, 250,200,fill="black", width=3, smooth=True,arrow="last")
            self.box1=self.cnv.create_rectangle(30,220,80,240)
            self.box2=self.cnv.create_rectangle(120,220,170,240)
            self.box3=self.cnv.create_rectangle(230,220,280,240)
            self.box4=self.cnv.create_rectangle(320,220,370,240)
            self.box5=self.cnv.create_rectangle(430,220,480,240)
            self.txt1=self.cnv.create_text(55,230,text='7',font=('Helvetica',15))
            self.txt2=self.cnv.create_text(145,230,text='8',font=('Helvetica',15))
            self.txt3=self.cnv.create_text(255,230,text='12',font=('Helvetica',15))
            self.txt4=self.cnv.create_text(345,230,text='37',font=('Helvetica',15))
            self.txt5=self.cnv.create_text(455,230,text='56',font=('Helvetica',15))
            self.page=1
        elif self.page==1:
            self.cnv.delete(self.titre)
            self.titre=self.cnv.create_text(250,120,text='Etape 2: fusion des 2 plus petits',font=('Helvetica', 20))
            self.fleche1 = self.cnv.create_line (250, 250, 250,330,fill="black", width=3, smooth=True,arrow="last")
            self.box6=self.cnv.create_rectangle(60,350,110,370)
            self.box61=self.cnv.create_rectangle(30,420,80,440)
            self.box62=self.cnv.create_rectangle(100,420,150,440)
            self.box7=self.cnv.create_rectangle(150,350,210,370)
            self.box8=self.cnv.create_rectangle(250,350,310,370)
            self.box9=self.cnv.create_rectangle(350,350,410,370)
            self.txt6=self.cnv.create_text(85,360,text='15',font=('Helvetica',15))
            self.txt61=self.cnv.create_text(55,430,text='7',font=('Helvetica',15))
            self.txt62=self.cnv.create_text(125,430,text='8',font=('Helvetica',15))
            self.txt7=self.cnv.create_text(180,360,text='12',font=('Helvetica',15))
            self.txt8=self.cnv.create_text(280,360,text='37',font=('Helvetica',15))
            self.txt9=self.cnv.create_text(380,360,text='56',font=('Helvetica',15))
            self.ligne1 = self.cnv.create_line (85, 370, 55,420,fill="black", width=3, smooth=True)
            self.ligne2 = self.cnv.create_line (85, 370, 125,420,fill="black", width=3, smooth=True)
            self.page=2
        elif self.page == 2:
            #remise à 0 du canvas
            self.cnv.pack_forget()
            self.cnv = tk.Canvas(self.wnd, width=dim*self.w, height=dim*self.h, bg='pink')
            self.cnv.pack(side=tk.LEFT)
            self.b1.pack_forget()
            self.b2.pack_forget()
            self.b3.pack_forget()
            self.b4.pack_forget()
            self.b5.pack_forget()
            self.quitte.pack_forget()
            self.b1.pack(side=(tk.RIGHT and tk.TOP),padx=5,pady=5)
            self.b2.pack(side=(tk.RIGHT and tk.TOP),padx=3,pady=5)
            self.b3.pack(side=(tk.RIGHT and tk.TOP),padx=5,pady=5)
            self.b4.pack(side=(tk.RIGHT and tk.TOP),padx=5,pady=5)
            self.b5.pack(side=(tk.RIGHT and tk.TOP),padx=5,pady=5)
            self.quitte.pack(side=(tk.RIGHT and tk.BOTTOM))
            #etape 3
            self.titre=self.cnv.create_text(250,50,text="Etape 3: réitération de la fusion jusqu'à avoir une paire:",font=('Helvetica', 15))
            #génération 1
            self.box1=self.cnv.create_rectangle(80,150,130,170)
            self.box2=self.cnv.create_rectangle(370,150,420,170)
            self.txt1=self.cnv.create_text(105,160,text='56',font=('Helvetica',15))
            self.txt2=self.cnv.create_text(395,160,text='64',font=('Helvetica',15))
            self.ligne1 = self.cnv.create_line (250, 100, 105, 150,fill="black", width=3, smooth=True)
            self.ligne2 = self.cnv.create_line (250, 100, 395,150,fill="black", width=3, smooth=True)
            #génération 2
            self.box3=self.cnv.create_rectangle(300,250,350,270)
            self.box4=self.cnv.create_rectangle(440,250,490,270)
            self.txt3=self.cnv.create_text(325,260,text='27',font=('Helvetica',15))
            self.txt4=self.cnv.create_text(465,260,text='37',font=('Helvetica',15))
            self.ligne3 = self.cnv.create_line (395, 170, 325,250,fill="black", width=3, smooth=True)
            self.ligne4 = self.cnv.create_line (395, 170, 465,250,fill="black", width=3, smooth=True)
            #génération 3
            self.box5=self.cnv.create_rectangle(230,350,280,370)
            self.box6=self.cnv.create_rectangle(370,350,420,370)
            self.txt5=self.cnv.create_text(255,360,text='12',font=('Helvetica',15))
            self.txt6=self.cnv.create_text(395,360,text='15',font=('Helvetica',15))
            self.ligne5 = self.cnv.create_line (325, 270, 255,350,fill="black", width=3, smooth=True)
            self.ligne6 = self.cnv.create_line (325, 270, 395,350,fill="black", width=3, smooth=True)
            #génération 4
            self.box7=self.cnv.create_rectangle(300,450,350,470)
            self.box8=self.cnv.create_rectangle(440,450,490,470)
            self.txt7=self.cnv.create_text(325,460,text='7',font=('Helvetica',15))
            self.txt8=self.cnv.create_text(465,460,text='8',font=('Helvetica',15))
            self.ligne7 = self.cnv.create_line (395, 370, 325,450,fill="black", width=3, smooth=True)
            self.ligne8 = self.cnv.create_line (395, 370, 465,450,fill="black", width=3, smooth=True)
            self.page=3
        elif self.page==3:
             self.cnv.delete('all')
             self.page=0

    def afficher_arbre(self):
        self.cnv.delete('all')
        #on fait choisir le fichier à l'utilisateur en limitant aux txt
        self.fichier = tkf.askopenfilename(title = "Selection du fichier")
        if(self.fichier == 'None'):
            return 0

        elif(self.fichier[-4:] != ".txt"):
            popupWindow = tk.Tk()
            popupWindow.wm_title("Window")
            labelBonus = tk.Label(popupWindow, text="Erreur le fichier n'est pas un .txt")
            labelBonus.grid(row=0, column=0)
            return 0

        liste = os.trier(self.fichier)
        # nous allons crée l'arbre
        #on trie la liste car elle n'arrive pas forcément trié
        occurances = [(ocurrance, lettre) for ocurrance,lettre in sorted\
                        (liste, key=lambda colonnes: colonnes[0])]

        self.arbre = ca.arbre(occurances)[0]
        self.recurence_affichage(self.arbre)

    def recurence_affichage(self,noeud, ligne=1):
        #je plonge dans l'arbre en testant si il y a des enfants
        #si il y a des enfants je rappel la fonction mais avec les enfants
        if (noeud.left != None):
            x = self.recurence_affichage(noeud.left, ligne)
            position_left = x[1:]
            ligne=x[0]
        if(noeud.right != None):
            x = self.recurence_affichage(noeud.right, ligne)
            position_right = x[1:]
            ligne=x[0]
        #si on est sur une feuille on affiche ces données key data et code
        if(noeud.left == None and noeud.right == None):
            self.txt1=self.cnv.create_text(20,60*ligne,text=str(noeud.data) + ' ' + str(noeud.key),font=('Helvetica',11))
            self.txt2=self.cnv.create_text(20,60*ligne+20,text=noeud.code,font=('Helvetica',11))
            position_x = 20
            position_y = 60*ligne+10
            ligne+=1
        else :
            position_x = max(position_left[0],position_right[0])+50
            position_y = min(position_left[1],position_right[1])+abs(position_left[1]-position_right[1])/2
            self.txt3=self.cnv.create_text(position_x,position_y,text=noeud.key,font=('Helvetica',11))
            self.ligne=self.cnv.create_line(position_left[0]+10,position_left[1],position_x-10,position_left[1],position_x-10,position_y)
            self.ligne=self.cnv.create_line(position_right[0]+10,position_right[1],position_x-10,position_right[1],position_x-10,position_y)

        return [ligne,position_x,position_y]


    def encoder(self):
        self.cnv.delete('all')
        #je récupere le fichier pour crée l'arbre de huffman
        self.fichier = tkf.askopenfilename(title = "Selection du fichier d'occurances")
        #je test si pas d erreur utilisateur
        if(self.fichier == 'None'):
            return 0

        elif(self.fichier[-4:] != ".txt"):
            popupWindow = tk.Tk()
            popupWindow.wm_title("Window")
            labelBonus = tk.Label(popupWindow, text="Erreur le fichier n'est pas un .txt")
            labelBonus.grid(row=0, column=0)
            return 0
        #je met soous le bon format
        liste = os.trier(self.fichier)
        occurances = [(ocurrance, lettre) for ocurrance,lettre in sorted\
                        (liste, key=lambda colonnes: colonnes[0])]

        x = [0 for i in range(len(occurances))]
        for i in range(len(occurances)):
            x[i]=occurances[i]

        couples = ca.code(occurances)
        #je demande le fichier qu'il veut encoder
        self.fichier_texte = tkf.askopenfilename(title = "Selection du fichier à encoder")
        #vérification et test de l'entré utilisateur
        if(self.fichier_texte == 'None'):
            return 0

        elif(self.fichier_texte[-4:] != ".txt"):
            popupWindow = tk.Tk()
            popupWindow.wm_title("Window")
            labelBonus = tk.Label(popupWindow, text="Erreur le fichier n'est pas un .txt")
            labelBonus.grid(row=0, column=0)
            return 0
        #je li le fichier et j'encode le texte
        try:
            with open(self.fichier_texte, encoding='utf-8', mode ='r') as fichier :
                self.texte = fichier.read()
        except IOError:
            print('error')
        texte_compresser = pc.codage(self.texte,couples)

        if texte_compresser == False :
            print("erreur un symbole du texte n'a pas de code associé")
        else:
            ef.encoder(texte_compresser,x)

        #affichage compression
        self.txt1=self.cnv.create_text(250,10,text='Fichier bien compresser',font=('Helvetica',11))
        self.txt2=self.cnv.create_text(250,30,text='Enregistrer sous byte.bin',font=('Helvetica',11))
        self.taille_texte = len(self.texte)
        with open('byte.bin', mode ='rb') as fichier :
                self.taille_texte_encod = fichier.read()
                self.taille_texte_encod = len(list(self.taille_texte_encod))
        #calcul taille compression
        rapport = (self.taille_texte_encod/self.taille_texte)*100
        self.txt3=self.cnv.create_text(150,60,text='Taille fichier décompressé',font=('Helvetica',11))
        self.box1=self.cnv.create_rectangle(120,80,170,280, fill='blue')
        taille_second_carre = 200 * (rapport/100)
        self.txt4=self.cnv.create_text(350,60,text='Taille fichier compressé',font=('Helvetica',11))
        #codee couleur pour identifier la réussite de la compréssion
        if(rapport <= 50):
            couleur = 'green'
        elif(rapport <= 60):
            couleur = 'yellow'
        elif(rapport <= 70):
            couleur = 'orange'
        elif(rapport > 70):
            couleur = 'red'
        self.box2=self.cnv.create_rectangle(320,80+(200-taille_second_carre),370,280, fill=couleur)
        self.txt5=self.cnv.create_text(150,320,text='Taille: ' + str(self.taille_texte) + ' octets',font=('Helvetica',11))
        self.txt6=self.cnv.create_text(350,320,text='Taille: ' + str(self.taille_texte_encod) + ' octets',font=('Helvetica',11))
        self.txt7=self.cnv.create_text(250,370,text='Pourcentage de réduction :',font=('Helvetica',11))
        self.txt8=self.cnv.create_text(250,400,text=str("{:.2f}".format(100-rapport))+'%',font=('Helvetica',11))


    def decoder(self):
        self.cnv.delete('all')
        #recupere le fichier a decoder
        self.fichier = tkf.askopenfilename(title = "select file to decode")
        #test si c esty pas vide ou dans le mauvais format
        if(self.fichier == 'None'):
            return 0

        elif(self.fichier[-4:] != ".bin"):
            popupWindow = tk.Tk()
            popupWindow.wm_title("Window")
            labelBonus = tk.Label(popupWindow, text="Erreur le fichier n'est pas un .bin")
            labelBonus.grid(row=0, column=0)
            return 0
        #j'appelle la fonction décoder
        texte = ef.decoder(self.fichier)

        self.txt1=self.cnv.create_text(250,10,text='Fichier bien décompresser',font=('Helvetica',11))
        self.txt2=self.cnv.create_text(250,30,text='Enregistrer sous fichier_décoder.txt',font=('Helvetica',11))
        #j'écris dans le fichier le texte décoder
        with open('fichier_décoder.txt',encoding='utf-8', mode ='w') as f :
            f.write(texte)

        with open('byte.bin',mode = 'rb') as f :
            taille_origine = f.read()

        #Calcul taille compression
        taille_origine = len(list(taille_origine))
        taille_texte = len(texte)
        rapport = (taille_origine/taille_texte)*100
        self.txt3=self.cnv.create_text(150,60,text='Taille fichier décompressé',font=('Helvetica',11))
        self.box1=self.cnv.create_rectangle(120,80,170,280, fill='blue')
        taille_second_carre = 200 * (rapport/100)
        self.txt4=self.cnv.create_text(350,60,text='Taille fichier compressé',font=('Helvetica',11))
        #code couleur pour identifier la réussite de la compréssion
        if(rapport <= 50):
            couleur = 'green'
        elif(rapport <= 60):
            couleur = 'yellow'
        elif(rapport <= 70):
            couleur = 'orange'
        elif(rapport > 70):
            couleur = 'red'
        self.box2=self.cnv.create_rectangle(320,80+(200-taille_second_carre),370,280, fill=couleur)
        self.txt5=self.cnv.create_text(150,320,text='Taille: ' + str(taille_texte) + ' octets',font=('Helvetica',11))
        self.txt6=self.cnv.create_text(350,320,text='Taille: ' + str(taille_origine) + ' octets',font=('Helvetica',11))
        self.txt7=self.cnv.create_text(250,370,text='Pourcentage de réduction :',font=('Helvetica',11))
        self.txt8=self.cnv.create_text(250,400,text=str("{:.2f}".format(100-rapport))+'%',font=('Helvetica',11))

Application()