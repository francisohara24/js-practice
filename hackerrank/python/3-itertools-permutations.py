# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


S, k = input().split()

results = permutations(sorted(S), int(k))

for result in results:
    result = "".join(result)
    print(result)
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


S, k = input().split()

results = permutations(sorted(S), int(k))

for result in results:
    result = "".join(result)
    print(result)
