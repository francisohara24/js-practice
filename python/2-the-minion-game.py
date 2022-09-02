def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    # compare scores
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)