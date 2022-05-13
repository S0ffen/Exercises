game = {1: "papper", 2:  "rock", 3:"scissors"}

while True:
    user1 = input("rock, papper or scissors: ").lower()
    user2 = input("rock, papper or scissors: ").lower()


    if user1 == game[1] and user2 == game[2]:
        print("Player 1 won")

    elif user1 == game[2] and user2 == game[1]:
        print("Player 2 won")
    
    elif user1 == game[2] and user2 == game[2]:
        print("Draw")

    elif user1 == game[1] and user2 == game[1]:
        print("Draw")

    elif user1 == game[3] and user2 == game[3]:
        print("Draw")

    elif user1 == game[3] and user2 == game[1]:
        print("Player 1 won")

    elif user1 == game[1] and user2 == game[3]:
        print("Player 2 won")

    elif user1 == game[2] and user2 == game[3]:
        print("Player 1 won")

    elif user1 == game[3] and user2 == game[2]:
        print("Player 2 won")

    asking = input("Continue? Yes or No: ").lower()
    if asking == "yes":
        continue
    elif asking == "no":
        break
    else:
        print("Wrong answer")
