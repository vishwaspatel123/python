import random
from name import words


def give_feedback(input_word, random_word):
    for x in input_word:
        print(x, end="  ")
    print()

    feedback = ""
    for i in range(len(input_word)):
        if input_word[i] == random_word[i]:
            feedback += "✔️ "  # Correct letter in the correct position
        elif input_word[i] in random_word:
            feedback += "❓ "  # Correct letter but in the wrong position
        else:
            feedback += "◼️ "  # Incorrect letter

    return feedback


def main():
    word = random.choice(words)
    print(word)
    print("Welcome to the word guessing game!")
    print("Try to guess the 5-letter word.")

    messages = {6: "Marvellous", 5: "Excellent", 4: "Very good", 3: "Nice", 2: "Good", 1: "Ok"}
    attempts_left = 7

    while attempts_left > 0:
        user_word = input("\nPlease enter a 5-letter word: ").strip()

        if len(user_word) == 5 and user_word.isalpha():
            attempts_left -= 1
            feedback = give_feedback(user_word, word)
            print(feedback)

            if user_word == word:
                print(f"\nCongratulations! {messages[attempts_left]}")
                break
        else:
            print("Invalid input. Make sure the word is exactly 5 letters and contains only letters.")

    if user_word != word:
        print(f"End of the game. The correct word was: {word}")


if __name__ == "__main__":
    main()
