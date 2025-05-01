input_file_opened = False
while not input_file_opened:
    try:
        file_name = input("Enter file name: ")
        with open(file_name, 'r') as f:
            lines = []
            target_word = input("Enter the word to replace: ")
            new_word = input("Enter the new word: ")
            total_replacements = 0

            for line in f:
                occ = line.count(target_word)
                newline = line.replace(target_word, new_word)
                lines.append(newline)
                total_replacements += occ
        input_file_opened = True

    except IOError:
        print('File not found - please re-enter')

nf = open(file_name, 'w')
for line in lines:
    nf.write(line)

nf.close()
print(f"\nAll occurrences of \"{target_word}\" have been replaced with \"{new_word}\".")
print(f"Total replacements made: {total_replacements}")
print(f"The changes have been saved in '{file_name}'.")