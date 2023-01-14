from itertools import combinations

S, k = input().split()
S = sorted(S)
k = int(k)
for i in range(1, k + 1):
    results = combinations(S, i)
    for result in results:
        print("".join(result))

