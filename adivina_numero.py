
number_to_guess = 2

user_number = int(input("Adivina un numero: "))

if number_to_guess == user_number:
    print ("Has ganado")
    print("Fin del juego")

else:
    print ("Has fallado intentalo otra vez")
    user_number = int(input("Adivina un numero: "))
    if number_to_guess == user_number:
        print("Has ganado")
        print("Fin del juego")

    else:
        print("Has fallado intentalo otra vez")
        user_number = int(input("Adivina un numero: "))
        if number_to_guess == user_number:
            print("Has ganado")
            print("Fin del juego")
        else:
            print("Has fallado intentalo una ultima vez vez")
            user_number = int(input("Adivina un numero: "))

            if number_to_guess == user_number:
                print("Has ganado")
                print("Fin del juego")
            else:
                print("Has perdido ")
                print("Fin del juego")










