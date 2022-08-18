# Alphabet Rangoli
def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    result = []
    final_result = []

    # catch corner case: 1
    if size == 1:
        print("a")
        return

    for i in reversed(range(size)):
        final_result.append(
            ("-".join(result) + "-" + alphabets[i] + "-" + "-".join(reversed(result))).center((4 * size - 3), "-"))
        result.append(alphabets[i])

    for i in range(size - 1):
        print(final_result[i])

    print(final_result[size - 1])

    for i in range(size - 2, -1, -1):
        print(final_result[i])


print_rangoli(26)

