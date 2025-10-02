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
    print(nb*2)

def exercice11():
    nb = int(input("Donnez un nombre : "))
    print("La moitié de ",nb," est : ",nb/2)

def exercice12():
    for i in range(5):
        print("Yo")


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

    else:
        print("Exercice non reconnu.")



if __name__ == "__main__":
    main()