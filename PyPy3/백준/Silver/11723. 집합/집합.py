import sys
input = sys.stdin.readline

x = int(input())
li = set()  
for i in range(x):
    inputs = input().split()
    a = inputs[0]
    
    if a in ["add", "check", "remove", "toggle"]:
        b = int(inputs[1])
    
    if a == "add":
        li.add(b) 
    elif a == "check":
        if b in li:
            print(1)
        else:
            print(0)
    elif a == "remove":
        li.discard(b)  # remove 
    elif a == "toggle":
        if b in li:
            li.remove(b)
        else:
            li.add(b)
    elif a == "all":
        li = set(range(1, 21))  
    elif a == "empty":
        li = set()  
