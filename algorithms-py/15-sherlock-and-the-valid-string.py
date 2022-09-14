def is_valid(s):
    n_times = []
    for char in set([i for i in s]):
        n_times.append(s.count(char))

    target = min(n_times)
    n_test = 0
    for i in n_times:
        if i != target:
            if i == (target + 1):
                n_test += 1
                if n_test > 1:
                    return "NO"
            else:
                return "NO"
    return "YES"


print(is_valid("aabbccddeefghi"))
