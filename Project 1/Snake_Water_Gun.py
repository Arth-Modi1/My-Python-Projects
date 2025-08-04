import random

print()
print("Snake = 1")
print("Water = 2")
print("Gun   = 3\n")

choices = {
    1 : "Snake",
    2 : "Water",
    3 : "Gun"}

you = int(input("Enter Your Choice: "))
print()
if you not in choices:
    print("Invalid choice! Please enter 1, 2, or 3.")
    exit()
print()
comp = random.randint(1, 3)

print(f"You Chose: {choices[you]}")
print(f"Computer Chose: {choices[comp]}")

if((you == 1 and comp == 2) or (you == 2 and comp == 3) or (you == 3 and comp == 1)):
    print("You Won!!")

elif((you == 1 and comp == 3) or (you == 2 and comp == 1) or (you == 3 and comp == 2)):
    print("You Lose!!")

elif((you == 1 and comp == 1) or (you == 2 and comp == 2) or (you == 3 and comp == 3)):
    print("It's a Tie!!")