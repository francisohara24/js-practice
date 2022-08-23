# The Minion Game
def substrings(string: str) -> set:
    """Returns a set of all possible substrings of a given string"""
    result = []
    for start in range(len(string)):
        for end in range(start, len(string)):
            result.append(string[start:end + 1])
    return set(result)  # remove duplicate substrings


def minion_game(string):
    # obtain score for stuart and kevin
    stuart = 0
    kevin = 0
    vowels = "AEIOU"
    for sub_str in substrings(string):
        main_str = string
        while sub_str in main_str:
            if sub_str[0] in vowels:
                kevin += 1
            else:
                stuart += 1
            main_str = main_str[main_str.find(sub_str) + 1:]

    # compare scores
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


minion_game("BANANA")
