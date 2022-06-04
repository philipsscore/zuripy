import random
choices = ["Rock", "Paper", "Scissors"]
CPU = random.choice(choices)

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

while True:
    print("Choice \n R for Rock, \n P for paper, and \n S for scissor \n")
    play = input("Enter R , P  or S ?").capitalize()
    if play == "R":
        player = "Rock"
    elif play == "P":
        player = "Paper"
    elif play == "S":
        player = "Scissors"
    else:
        print("Wrong value, you Entered ", play.lower(), " try again with R, P or S",)
        continue

    
    if player == CPU:
        print("Tie!")
    elif player == "Rock":
        if CPU == "Paper":
            print("Computer Win!", CPU, "covers", player)
            
        else:
            print("You win!", player, "smashes", CPU)
            
    elif player == "Paper":
        if CPU == "Scissors":
            print("computer Win!", CPU, "cut", player)
            
        else:
            print("You win!", player, "covers", CPU)
            
    elif player == "Scissors":
        if CPU == "Rock":
            print("Computer...", CPU, "smashes", player)
            
        else:
            print("You win!", player, "cut", CPU)
            

    break