b=0
for i in range(5):
    a=int(input())
    if a<40:
        b+=40
    else:
        b+=a
print(f'{b/5:.0f}')