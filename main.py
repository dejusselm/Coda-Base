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
        
    else:
        print("Exercice non reconnu.")



if __name__ == "__main__":
    main()