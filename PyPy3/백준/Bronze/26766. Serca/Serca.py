# Define the heart pattern
heart_pattern = [
    " @@@   @@@ ",
    "@   @ @   @",
    "@    @    @",
    "@         @",
    " @       @ ",
    "  @     @  ",
    "   @   @   ",
    "    @ @    ",
    "     @     "
]

# Read the number of hearts (N)
N = int(input())

# Output the hearts N times
for i in range(N):
    print("\n".join(heart_pattern))
