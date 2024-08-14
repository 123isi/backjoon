x = int(input())
result = x

for i in range(x):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result -= 1
            break

print(result)