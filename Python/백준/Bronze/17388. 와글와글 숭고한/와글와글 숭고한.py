university = list(map(int, input().split()))

if sum(university) >= 100:
    print("OK")
else:
    check = university.index(min(university))
    if check == 0:
        print("Soongsil")
    elif check == 1:
        print("Korea")
    elif check == 2:
        print("Hanyang")
