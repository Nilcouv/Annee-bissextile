# rejouer le programme
replay = True
while replay:
    # Entrée d'une réponse
    year = int(input("saisissez une année : "))
    print("Vous avez sélectionné l'année : ", year)
    
    # test de l'année
    bissextile=False

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        bissextile=True
    else:
        bissextile=False

    # impression du résultat
    if bissextile:
        print("l'année", year, "est une année bissextile")       
    else:
        print("l'année", year, "n'est pas une année bissextile")

    # Rejouer le programme
    loop2=True
    while loop2:
        print("Voulez vous tester une autre année? \n 1) Oui \n 2) Non")
        answer = input("Réponse : ")

        if answer == "1" or answer == "Oui" or answer == "oui":
            loop2 = False
            replay = True
        elif answer == "2" or answer == "Non" or answer == "non":
            loop2 = False
            replay = False
        else:
            print("Veuillez entrer une réponse valide!")

#fin du programme
input("Appuyez sur ENTRÉE pour fermer le programme.")
