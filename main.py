def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    nom = input('Quel est votre nom ? ')
    print("Bonjour ",nom," !")

def exercice3():
    print("Bonjour \n le \n monde")

def exercice4():
    annee = int(input('Quelle est votre année de naissance ? '))
    print("Vous avez environ ",2025-annee," ans")

def exercice5():
    nb1 = int(input("Donnez un premier nombre : "))
    nb2 = int(input("Donnez un deuxième nombre : "))
    print(nb1+nb2)

def exercice6():
    nb1 = int(input("Donnez un premier nombre : "))
    nb2 = int(input("Donnez un deuxième nombre : "))
    print(nb1-nb2)

def exercice7():
    nb1 = int(input("Donnez un premier nombre : "))
    nb2 = int(input("Donnez un deuxième nombre : "))
    print(nb1*nb2)

def exercice8():
    nb1 = int(input("Donnez un premier nombre : "))
    nb2 = int(input("Donnez un deuxième nombre : "))
    print(nb1//nb2)

def exercice9():
    nb = int(input("Donnez un nombre : "))
    print(nb**2)

def exercice10():
    nb = int(input("Donnez un nombre : "))
    print("Le double de ",nb, "est ",nb*2)

def exercice11():
    nb = int(input("Donnez un nombre : "))
    print("La moitié de ",nb," est : ",nb/2)

def exercice12():
    for i in range(5):
        print("Yo")

def exercice13():
    for i in range(1,6):
        print(i)

def exercice14():
    for i in range(1,6):
        print("2 x ",i," = ", 2*i)

def exercice15():
    long= int(input("Donnez la longueur du côté du carré : "))
    print("Périmètre = ",4*long)

def exercice16():
    long= int(input("Donnez la longueur du côté du carré : "))
    print("Aire = ",long*long)

def exercice17():
    quant=int(input("Indiquer la somme à convertir : "))
    print(quant,"€ = ", quant*1.1, "$")

def exercice18():
    temps=int(input("Indiquer une durée (en min) : "))
    print(temps," minutes = ",temps*60," secondes")

def exercice19():
    prix=int(input("Indiquer un prix HT : "))
    print("Prix TTC = ",prix+prix*(20/100))

def exercice20():
    nom = input("Donner un nom : ")
    age = input("Donner un âge : ")
    print(nom, "a ",age," ans.")

def exercice21():
    nb = int(input("Donner un nombre : "))
    if nb>0:
        print("Le nombre est positif.")
    elif nb<0:
        print("Le nombre est négatif.")
    else:
        print("Le nombre est nul.")

def exercice22():
    age = int(input("Donner un âge : "))
    if age>=18:
        print("La personne est majeure.")
    else :
        print("La personne est mineure.")

def exercice23():
    note = int(input("Donner une note : "))
    if note >=12:
        print("Validé")
    else :
        print("Non validé")

def exercice24():
    nb1 = int(input("Donner un premier nombre : "))
    nb2 = int(input("Donner un deuxième nombre : "))
    if nb1 >nb2:
        print(nb1, " est plus grand.")
    elif nb2 >nb1:
        print(nb2, " est plus grand.")
    else :
        print("Les deux nombres sont égaux.")

def exercice25():
    nb1 = int(input("Donner un premier nombre : "))
    nb2 = int(input("Donner un deuxième nombre : "))
    if nb1 <nb2:
        print("Ordre croissant : OUI")
    elif nb1 >nb2:
        print("Ordre croissant : NON")
    else:
        print("Tous les nombres sont égaux.")
    

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()   
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7() 
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    elif choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    else:
        print("Exercice non reconnu.")



if __name__ == "__main__":
    main()