# Read input values
s1, s2 = map(int, input().split())

# Check if the problem is considered easy
if s1 >= s2 / 2:
    print("E")  # Easy
else:
    print("H")  # Hard
