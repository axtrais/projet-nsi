import random
e=0
d=0
b=0

print("à quelle jeux voulez vous jouer?")        #selection dui jeux
print("taper 1 pour jouer à pierre feuille ciseaux")
a=int(input("taper 2 pour jouer au morpion:"))


if a==1:
    print("pour utiliser la pierre taper 1")      #fonctionnement du jeux
    print("pour utiliser feuille taper 2")
    print("pour utiliser le ciseaux taper 3")
    print("taper 4 pour arrêter")
    while b<4:
         b=int(input(":"))
         c=random.randint(1,3)
         
         
         if b==1 and c==2:         # condition de victoire
             e=e+1
             print("le bot a gagner en utilisant feuille re essayer")
         if b==1 and c==3:
            d=d+1
            print("vous avez gagner contre le bot qui a utiliser ciseaux!!")
         if b==2 and c==1 :
            d=d+1
            print("vous avez gagner contre le bot qui a utiliser pierre!!")
         elif b==2 and c==3 :
            e=e+1
            print("le bot a gagner en utilisant ciseaux re essayer")
         if b==3 and c==1:
             e=e+1
             print("le bot a gagner en utilisant pierre re essayer")
         elif b==3 and c==2:
            d=d+1
            print("vous avez gagner contre le bot qui a utiliser feuille!!")
         elif b==c :
            print("vous avez fait égaliter")
            
    print("Voici les scores:")      #score finale
    print("vous avez un score de",d)
    print("le bot a un score de",e)
    
    
if a==2:
    def afficher_grille(grille):            # affichage du morpion avec les lignes et les collones
        print("     0)  1)  2)")
        print("   -------------")
        print("0)", end='')
        
        for i in range(3):
            print(" | "+str(grille[i]), end='')
        print(" |")
        print("   -------------")
        print("1)", end='')
        
        for i in range(3):
            print(" | "+str(grille[i+3]), end='')
        print(" |")
        print("   -------------")
        print("2)", end='')
        
        for i in range(3):
            print(" | "+str(grille[i+6]), end='')
        print(" |")
        print("   -------------")


    def tour(grille, joueur):         # permet de saisir la case jouer lors du tours
        print("C'est le tour du joueur "+str(joueur))
        colonne=input("Entrez le numero de la colonne : ")
        ligne=input("Entrez le numero de la ligne : ")
        print("Vous avez joué la case ("+colonne+","+ligne+")")
        
        while grille[int(colonne)+int(ligne)*3]!=" ":          #sert a vérifier si la case est déjà
            afficher_grille(grille)
            print("Cette case est deja jouée ! Saisissez une autre case svp !")
            colonne=input("Entrez le numero de la colonne : ")
            ligne=input("Entrez le numero de la ligne : ")
            print("Vous avez joué la case ("+colonne+","+ligne+")")

        if joueur==1 :
            grille[int(colonne)+int(ligne)*3]="X"
        if joueur==2 :
            grille[int(colonne)+int(ligne)*3]="O"
        afficher_grille(grille)

    def est_gagnant(grille):          # condition de victoire
        if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
            return 1
        if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
            return 1
        if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
            return 1
        if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
            return 1
        if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
            return 1
        if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
            return 1
        if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
            return 1
        if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
            return 1


    def est_match_nul(grille):      # termine le match si c'est égaliter
        for i in range(9):
            if grille[i]==" ":
                return 0
        return 1

    joueur=1
    print("Le joueur 1 possède les X. Le joueur 2 possède les O")
    grille=[" "," "," "," "," "," "," "," "," "]
    afficher_grille(grille)
    gagne=0
    while gagne==0:            # message de victoire
        tour(grille,joueur)
        if est_gagnant(grille):
            print("Le joueur "+str(joueur)+" remporte la partie")
            gagne=1
        else:
            if est_match_nul(grille):      # message d'égaliter
                print("Plus de place ! Match nul !")
                gagne=1
        if joueur==1:
            joueur=2
        else:
            joueur=1
