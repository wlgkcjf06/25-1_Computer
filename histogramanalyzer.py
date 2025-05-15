VOWELS = set("aeiou")

def load_text_file(filename="text.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def build_histogram(text):
    histogram = {}
    text = text.lower()
    for k in text:
        if k in histogram.keys() and k.isalpha() == True:
            histogram[k]+=1
        elif k.isalpha() == True:
            histogram[k]=1
    return histogram

def display_char_frequency(histogram, target_char):
    total_letters = sum(histogram.values())
    freq = histogram[target_char]
    ratio = freq / total_letters * 100
    print(f"Frequency of '{target_char}': {freq}")
    print(f"Ratio of '{target_char}': {ratio:.2f}%")

def analyze_vowel_consonant_ratio(histogram):
    total = sum(histogram.values())
    v_ratio = 0
    c_ratio = 0
    for letter in VOWELS:
        if letter in histogram.keys():
            v_ratio += histogram[letter]
    v_ratio = v_ratio / total * 100
    c_ratio = 100 - v_ratio
    print(f"Ratio of vowels: {v_ratio:.2f}%")
    print(f"Ratio of consonants: {c_ratio:.2f}%")

def can_construct_word(histogram, word):
    temp = histogram.copy()
    can_construct = True
    for letter in word:
        if letter not in temp.keys():
            can_construct = False
            break
        elif temp[letter] == 0:
            can_construct = False
            break
        else:
            temp[letter]-=1
    if can_construct:
        print(f"Can construct '{word}' from histogram.")
    else:
        print(f"Cannot construct '{word}' from histogram.")


def main():
    text = load_text_file()
    histogram = build_histogram(text)
    while True:
        print("\nChoose an option:")
        print("1. Frequency of a specific character")
        print("2. Vowel/Consonant ratio analysis")
        print("3. Can a word be constructed from text?")
        print("0. Exit")
        option = input("Enter option: ").strip()
        if option == "1":
            ch = input("Enter the character: ").strip().lower()
            display_char_frequency(histogram, ch)
        elif option == "2":
            analyze_vowel_consonant_ratio(histogram)
        elif option == "3":
            word = input("Enter the word: ").strip().lower()
            can_construct_word(histogram, word)
        elif option == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()