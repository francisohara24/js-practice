
def anagram(s):
    result = 0
    previous = ""
    first = s[:len(s)//2]
    second = s[len(s)//2:]
    if len(s) % 2 == 1: return -1
    for char in first:
        if char not in previous:
            result += abs(first.count(char) - second.count(char))
            previous = previous + char
    return result

print(anagram("fdhlvosfpafhalll"))
