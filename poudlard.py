print("""Vous aurez une suite de question qui vous permetterons de voir a quelle Maison vous pourriez appartenir.
      
      Répondez simplement par A, B, C ou D avec la majusucle.""")

one = input("""Quel est votre sujet préféré:
            
        A. Métamorphose
        B. Potions
        C. Botanique
        D. Charmes
        
        > """)
two = input("""Quelle est votre couleur favorite:
            
        A. Rouge
        B. Vert
        C. Orange
        D. Bleu
        
        > """)
three = input("""Si vous pouviez uniquement faire une de ces choses dans votre vie, laquelle feriez vous:
            
        A. Voyager et Explorer
        B. Commencer un Business
        C. Rester avec la famille
        D. Apprendre
        
        > """)
four = input("""Quel animal choisirez vous:
        A. Chat
        B. Lézard
        C. Chien
        D. Perroquet
        
        > """)

five = input("""Quel mot vous décrit le mieux:
            
        A. Aventureux
        B. Rusé
        C. Amical
        D. Intelligent
        
        > """)

six = input("""Qui pourrait être votre meilleur ami a Poudlard:
        
        A. Ron Weasley
        B. Harry Potter
        C. Neville Longbottom
        D. Hermione Granger
        
        > """)

seven = input("""Si vous voyez votre ami tricher, que feriez vous:
        A. Regarder autre part et continuer
        B. Laisser le tricher sur vous la prochaine fois
        C. Le dire au professeur
        D. L'aider pour la prochaine fois
        
        > """)

eight = input("""Lequel est votre fantôme préféré a Poudlard:
            
            A. Nearly-Headless Nick
            B. Bloody Baron
            C. Fat Friar
            D. Grey Lady
            
        > """)

nine = input("""Quel animal aimeriez vous être:
            
            A. Chat
            B. Panthère
            C. Loutre
            D. Loup
            
        > """)
   
points = 0

if one == "A":
    points += 1
elif one == "B":
    points += 2
elif one == "C":
    points += 3
elif one == "D":
    points += 4

if two == "A":
    points += 1
elif two == "B":
    points += 2
elif two == "C":
    points += 3
elif two == "D":
    points += 4

if three == "A":
    points += 1
elif three == "B":
    points += 2
elif three == "C":
    points += 3
elif three == "D":
    points += 4

if four == "A":
    points += 1
elif four == "B":
    points += 2
elif four == "C":
    points += 3
elif four == "D":
    points += 4

if five == "A":
    points += 1
elif five == "B":
    points += 2
elif five == "C":
    points += 3
elif five == "D":
    points += 4

if six == "A":
    points += 1
elif six == "B":
    points += 2
elif six == "C":
    points += 3
elif six == "D":
    points += 4

if seven == "A":
    points += 1
elif seven == "B":
    points += 2
elif seven == "C":
    points += 3
elif seven == "D":
    points += 4

if eight == "A":
    points += 1
elif eight == "B":
    points += 2
elif eight == "C":
    points += 3
elif eight == "D":
    points += 4

if nine == "A":
    points += 1
elif nine == "B":
    points += 2
elif nine == "C":
    points += 3
elif nine == "D":
    points += 4

if points == 9:
    print("Vous appertenez à la maison: Gryffondor, bravo !")
if points == 10:
    print("Vous appertenez à la maison: Gryffondor, bravo !")
if points == 11:
    print("Vous appertenez à la maison: Gryffondor, bravo !")
if points == 12:
    print("Vous appertenez à la maison: Gryffondor, bravo !")
if points == 13:
    print("Vous appertenez à la maison: Gryffondor, bravo !")
if points == 14:
    print("Vous appertenez à la maison: Gryffondor, bravo !")
if points == 15:
    print("Vous appertenez à la maison: Gryffondor, bravo !")

if points == 16:
    print("Vous appertenez à la maison: Serpentard, bravo !")
if points == 17:
    print("Vous appertenez à la maison: Serpentard, bravo !")
if points == 18:
    print("Vous appertenez à la maison: Serpentard, bravo !")
if points == 19:
    print("Vous appertenez à la maison: Serpentard, bravo !")
if points == 20:
    print("Vous appertenez à la maison: Serpentard, bravo !")
if points == 21:
    print("Vous appertenez à la maison: Serpentard, bravo !")
if points == 22:
    print("Vous appertenez à la maison: Serpentard, bravo !")

if points == 23: 
    print("Vous appertenez à la maison: Poufsouffle, bravo !")
if points == 24: 
    print("Vous appertenez à la maison: Poufsouffle, bravo !")
if points == 25: 
    print("Vous appertenez à la maison: Poufsouffle, bravo !")
if points == 26: 
    print("Vous appertenez à la maison: Poufsouffle, bravo !")
if points == 27: 
    print("Vous appertenez à la maison: Poufsouffle, bravo !")
if points == 28: 
    print("Vous appertenez à la maison: Poufsouffle, bravo !")
if points == 29: 
    print("Vous appertenez à la maison: Poufsouffle, bravo !")

if points == 30:
    print("Vous appertenez à la maison: Serdaigle, bravo !")
if points == 31:
    print("Vous appertenez à la maison: Serdaigle, bravo !")
if points == 32:
    print("Vous appertenez à la maison: Serdaigle, bravo !")
if points == 33:
    print("Vous appertenez à la maison: Serdaigle, bravo !")
if points == 34:
    print("Vous appertenez à la maison: Serdaigle, bravo !")
if points == 35:
    print("Vous appertenez à la maison: Serdaigle, bravo !")

print("Avec un total de " + str(points) + "points.")