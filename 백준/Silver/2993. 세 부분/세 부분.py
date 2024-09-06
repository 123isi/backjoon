word = input()

best_word = None

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        part1 = word[:i]
        part2 = word[i:j]
        part3 = word[j:]

        new_word = part1[::-1] + part2[::-1] + part3[::-1]

        if best_word is None or new_word < best_word:
            best_word = new_word

print(best_word)
