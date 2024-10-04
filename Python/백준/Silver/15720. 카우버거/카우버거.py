a, b, c = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
li3 = list(map(int, input().split()))

li1.sort(reverse=True)
li2.sort(reverse=True)
li3.sort(reverse=True)

lengths = [len(li1), len(li2), len(li3)]
lengths.sort()
result = 0
max_value = 0

for i in range(lengths[0]):
    a = 0
    if i < len(li1):
        a += li1[i]
    if i < len(li2):
        a += li2[i]
    if i < len(li3):
        a += li3[i]
    
    max_value += a
    result += a * 0.9

for lst in (li1, li2, li3):
    for i in range(len(lst)):
        if i >= lengths[0]:  
            max_value += lst[i]
            result += lst[i]

print(max_value)
print(f'{result:.0f}')
