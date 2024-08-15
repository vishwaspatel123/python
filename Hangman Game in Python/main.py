import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(" ")

word = random.choice(someWords)

if __name__ == "__main__":
    print('Guess the word! HINT: word is a name of a fruit')
    for i in word:
        print("_",end=" ")
    print()

    correct = 0
    letterGuessed = ''
    chances = len(word) + 2
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("enter only one letter")
                continue
            elif guess in letterGuessed:
                print("u already enter the letter")
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed and Counter(letterGuessed) != Counter(word):
                    print(char, end=' ')
                    correct += 1
                elif Counter(letterGuessed) == Counter(word):
                    print(f" the word is {word}")
                    flag = 1
                    print("YOU win the game")
                    break
                    break
                else:
                    print("_",end=" ")

        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print()
            print("YOU lost the game")
            print(f"the word is {word}")

    except KeyboardInterrupt:
        print()
        print("bye! try again")
        print()


