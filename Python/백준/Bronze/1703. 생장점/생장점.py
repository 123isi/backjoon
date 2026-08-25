while True:
    data = input()
    if data == "0": break
    else: data = data.split(" ")
    a = int(data[0])
    data = list(map(int, data[1:]))
    original = 1
    sum = 0
    for i in range(a):
        original *= data[2*i]
    for i in range(1, a+1):
            multiply = 1
            multiply *= data[2*i-1]
            for k in range(i, a):
                multiply *= data[2*k]
            sum += multiply
    print(original - sum)