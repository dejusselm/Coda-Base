def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    nom = input('Quel est votre nom ? ')
    print("Bonjour ",nom," !")

def exercice3():
    print("Bonjour \n le \n monde")

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    else:
        print("Exercice non reconnu.")


if __name__ == "__main__":
    main()