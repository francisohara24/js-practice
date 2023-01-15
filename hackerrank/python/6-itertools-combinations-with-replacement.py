# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S, k = input().split()
S = sorted(S)
k = int(k)

answers = combinations_with_replacement(S, k)

for answer in answers:
    print("".join(answer))
