def highest_value_palindrome(s, n, k):
    changes_req = []
    i = 0
    while i < (n - 1) / 2:
        if s[i] != s[n - 1 - i]:
            changes_req.append(i)
        i += 1

    if len(changes_req) > k:
        return -1
    elif len(changes_req) == k:
        for i in changes_req:
            if s[i] > s[n - 1 - i]:
                s = s[:n - 1 - i] + s[i] + s[n - i:]
            else:
                s = s[:i] + s[n - 1 - i] + s[i + 1:]
        return s
    else:
        pass


print(highest_value_palindrome("12361", 5, 1))