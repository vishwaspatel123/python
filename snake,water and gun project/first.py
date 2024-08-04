import random
def generate_random_number():
    return random.choice([1, 0, -1])

print("hello gamer")
print("This is snake water and gun game")

while(True):
    int = input("do you want to pay the game if u want to play then press 1 else 0")
    if(int == "1"):
        random_number = generate_random_number()
        computerdict = {
            -1: "snake",
            1: "water",
            0: "gun"
        }
        computerinput = computerdict[random_number]
        user = input("enter you Choose").strip().lower()
        print(f"computer input is {computerinput} ")
        if (computerinput == user):
                print("It is a draw")
        else:
            if (user == "snake" and computerinput == "water"):
                    print("u win")
            elif (user == "snake" and computerinput == "gun"):
                    print("u loss")
            elif (user == "water" and computerinput == "gun"):
                    print("u win")
            elif (user == "water" and computerinput == "snake"):
                    print("u loss")
            elif (user == "gun" and computerinput == "water"):
                    print("u loss")
            elif (user == "gun" and computerinput == "snake"):
                    print("u win")
            else:
                print("something went wrong")
    else:
        print("thank you")
        break
