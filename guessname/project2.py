import random
from name import words

def iswords(input_word,ramdom):
    for x in input_word:
        print(x, end=" ")
    print()

    for i in range(len(input_word)):
        if input_word[i] == ramdom[i]:
            print("?",end=" ")
        elif input_word[i] in ramdom:
            print("?",end=" ")
        else:
            print("◼️",end="")

    if input_word == ramdom:
        return 1
    else:
        return 0


word = random.choice(words)
print(word)
print("hello,how are u")
print("welcome to the game of words guess")
message, i = {6: "Marvellous", 5: "Excellent", 4: "Very good", 3: "Nice", 2: "Good", 1: "Ok"}, 7
while i > 0:
    user_words = input("\npls enter a word of 5 letter")
    if(len(user_words) == 5 and user_words.isalpha()):
        i = i - 1
        if iswords(user_words , word):
            print("\n",message[i])
            break
        else:
            continue
    else:
        print("u enter a in valid word")

print(f"end of the game the correct words is {word}")