# The Minion Game

def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    length = len(string)
    start = 0
    while start < length:
        end = start
        while end < length:
            if string[start] in vowels:
                kevin += 1
            else:
                stuart += 1
            end += 1
        start += 1

    # compare scores
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


minion_game(input())
