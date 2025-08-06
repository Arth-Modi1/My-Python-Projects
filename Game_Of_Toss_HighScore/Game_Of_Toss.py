import random

print("Let's play a Game!")
print("You Have to GUess Whether it is Heads or Tails!")
print("Heads = 0")
print("Tails = 1")
print("")

def game(score):
    comp = random.randint(0,1)

    player = int(input("Enter Your Guess (0/1): "))
    print("")

    if(player == comp):
        print("You Won!")
        score += 1
        play_again = input("Do You Want To Play Again (y/n): ")

        if(play_again == "y"):
            game(score)

        elif(play_again == "n"):
            print("Thanks For Playing!")
            print(f"Your Score is {score}")

    elif player not in [0,1]:
        print("Invalid Input!")
        print("Try Again!")

    else:
        print("You Lose!")
        print(f"Your Score is {score}")

    with open("hi_score.txt") as f:
        hi_score = f.read()

        if (hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0

    if(score > hi_score):
        print("Woahh!! You Just Made A High Score!")
        with open("hi_score.txt", "w") as f:
            f.write(str(score))
        

game(score=0)
