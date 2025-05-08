import random

def load_words():
    words = []
    try:
        f = open('words.txt', 'r')
        line = f.readline()
        while line != '':
            words.append(line.upper().strip())
            line = f.readline()
        f.close()
    except IOError:
        print("Could not find words.txt.")
        return []
    return words

def choose_word(words):
    return random.choice(words)

def display_progress(answer, guessed_letters):
    display_word = ""
    letters = list(answer)
    for i in range(len(letters)):
        if not letters[i] in guessed_letters:
            letters[i] = ''
    for k in letters:
        if k == '':
            display_word = display_word+ '_ '
        else:
            display_word = display_word + k + ' '
    return display_word.strip()

def play_game():
    words = load_words()
    if len(words) == 0:
        print("No words available to play.")
        return
    answer = choose_word(words)
    guessed_letters = []
    attempts_left = 6
    print("🎮 Welcome to the Word Guessing Game! You have 6 chances.")
    print(f"Hint: The word has {len(answer)} letters.")
    while attempts_left > 0:
        print("\nCurrent word:", display_progress(answer, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Enter a letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single alphabet letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in answer:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            attempts_left -= 1
        flag = True
        for k in list(answer):
            if not k in guessed_letters:
                flag = False

        if flag:
            print(f"\n🎉 Congratulations! You guessed the word: '{answer}'")
            break
    else:
        print(f"\n💀 Game over! The correct word was: '{answer}'")

if __name__ == "__main__":
    play_game()