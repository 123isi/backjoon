alphabet_count = [0] * 26
S = input()
for char in S:
    alphabet_count[ord(char) - ord('a')] += 1
print(' '.join(map(str, alphabet_count)))
