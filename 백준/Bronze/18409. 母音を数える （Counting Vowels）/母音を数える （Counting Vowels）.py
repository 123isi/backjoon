n = int(input())
s = input().strip()
vowels = set('aeiou')
count = sum(1 for char in s if char in vowels)
print(count)