"""Script that generates all 44 sub-keys for 10-round (128-bit) AES Encryption Algorithm"""


def default_key(string):
    result = []
    result_hex = []
    answer = []
    answer_hex = ""
    for char in string:
        binary = bin(ord(char))[2:].rjust(8, "0")
        hexadecimal = hex(int(binary, 2))[2:]
        print(char, " = ", binary, " = ", hexadecimal)
        answer.append(binary)
        answer_hex += hexadecimal
        if len(answer) >= 4:
            result.append(answer)
            result_hex.append(answer_hex)
            answer = []
            answer_hex = ""
    print("\nW0 - W3\n———————————")
    print(f"W0 {result_hex[0]}")
    print(f"W1 {result_hex[1]}")
    print(f"W2 {result_hex[2]}")
    print(f"W3 {result_hex[3]}\n\n")
    return result


def sub_key(round_no, words):
    # For labelling results in each round
    zero = 4 * (round_no - 1)
    one = zero + 1
    two = one + 1
    three = two + 1

    # round constants to be XORed in each round
    round_constants = {1: "00000001000000000000000000000000", 2: "00000010000000000000000000000000",
                       3: "00000100000000000000000000000000",
                       4: "00001000000000000000000000000000", 5: "00010000000000000000000000000000",
                       6: "00100000000000000000000000000000",
                       7: "01000000000000000000000000000000", 8: "10000000000000000000000000000000",
                       9: "00011011000000000000000000000000",
                       10: "00110110000000000000000000000000"}

    # Rijndael S-Box
    s_box = {'00': '63', '01': '7c', '02': '77', '03': '7b', '04': 'f2', '05': '6b', '06': '6f', '07': 'c5', '08': '30',
             '09': '01', '0a': '67', '0b': '2b', '0c': 'fe', '0d': 'd7', '0e': 'ab', '0f': '76', '10': 'ca', '11': '82',
             '12': 'c9', '13': '7d', '14': 'fa', '15': '59', '16': '47', '17': 'f0', '18': 'ad', '19': 'd4', '1a': 'a2',
             '1b': 'af', '1c': '9c', '1d': 'a4', '1e': '72', '1f': 'c0', '20': 'b7', '21': 'fd', '22': '93', '23': '26',
             '24': '36', '25': '3f', '26': 'f7', '27': 'cc', '28': '34', '29': 'a5', '2a': 'e5', '2b': 'f1', '2c': '71',
             '2d': 'd8', '2e': '31', '2f': '15', '30': '04', '31': 'c7', '32': '23', '33': 'c3', '34': '18', '35': '96',
             '36': '05', '37': '9a', '38': '07', '39': '12', '3a': '80', '3b': 'e2', '3c': 'eb', '3d': '27', '3e': 'b2',
             '3f': '75', '40': '09', '41': '83', '42': '2c', '43': '1a', '44': '1b', '45': '6e', '46': '5a', '47': 'a0',
             '48': '52', '49': '3b', '4a': 'd6', '4b': 'b3', '4c': '29', '4d': 'e3', '4e': '2f', '4f': '84', '50': '53',
             '51': 'd1', '52': '00', '53': 'ed', '54': '20', '55': 'fc', '56': 'b1', '57': '5b', '58': '6a', '59': 'cb',
             '5a': 'be', '5b': '39', '5c': '4a', '5d': '4c', '5e': '58', '5f': 'cf', '60': 'd0', '61': 'ef', '62': 'aa',
             '63': 'fb', '64': '43', '65': '4d', '66': '33', '67': '85', '68': '45', '69': 'f9', '6a': '02', '6b': '7f',
             '6c': '50', '6d': '3c', '6e': '9f', '6f': 'a8', '70': '51', '71': 'a3', '72': '40', '73': '8f', '74': '92',
             '75': '9d', '76': '38', '77': 'f5', '78': 'bc', '79': 'b6', '7a': 'da', '7b': '21', '7c': '10', '7d': 'ff',
             '7e': 'f3', '7f': 'd2', '80': 'cd', '81': '0c', '82': '13', '83': 'ec', '84': '5f', '85': '97', '86': '44',
             '87': '17', '88': 'c4', '89': 'a7', '8a': '7e', '8b': '3d', '8c': '64', '8d': '5d', '8e': '19', '8f': '73',
             '90': '60', '91': '81', '92': '4f', '93': 'dc', '94': '22', '95': '2a', '96': '90', '97': '88', '98': '46',
             '99': 'ee', '9a': 'b8', '9b': '14', '9c': 'de', '9d': '5e', '9e': '0b', '9f': 'db', 'a0': 'e0', 'a1': '32',
             'a2': '3a', 'a3': '0a', 'a4': '49', 'a5': '06', 'a6': '24', 'a7': '5c', 'a8': 'c2', 'a9': 'd3', 'aa': 'ac',
             'ab': '62', 'ac': '91', 'ad': '95', 'ae': 'e4', 'af': '79', 'b0': 'e7', 'b1': 'c8', 'b2': '37', 'b3': '6d',
             'b4': '8d', 'b5': 'd5', 'b6': '4e', 'b7': 'a9', 'b8': '6c', 'b9': '56', 'ba': 'f4', 'bb': 'ea', 'bc': '65',
             'bd': '7a', 'be': 'ae', 'bf': '08', 'c0': 'ba', 'c1': '78', 'c2': '25', 'c3': '2e', 'c4': '1c', 'c5': 'a6',
             'c6': 'b4', 'c7': 'c6', 'c8': 'e8', 'c9': 'dd', 'ca': '74', 'cb': '1f', 'cc': '4b', 'cd': 'bd', 'ce': '8b',
             'cf': '8a', 'd0': '70', 'd1': '3e', 'd2': 'b5', 'd3': '66', 'd4': '48', 'd5': '03', 'd6': 'f6', 'd7': '0e',
             'd8': '61', 'd9': '35', 'da': '57', 'db': 'b9', 'dc': '86', 'dd': 'c1', 'de': '1d', 'df': '9e', 'e0': 'e1',
             'e1': 'f8', 'e2': '98', 'e3': '11', 'e4': '69', 'e5': 'd9', 'e6': '8e', 'e7': '94', 'e8': '9b', 'e9': '1e',
             'ea': '87', 'eb': 'e9', 'ec': 'ce', 'ed': '55', 'ee': '28', 'ef': 'df', 'f0': '8c', 'f1': 'a1', 'f2': '89',
             'f3': '0d', 'f4': 'bf', 'f5': 'e6', 'f6': '42', 'f7': '68', 'f8': '41', 'f9': '99', 'fa': '2d', 'fb': '0f',
             'fc': 'b0', 'fd': '54', 'fe': 'bb', 'ff': '16'}

    W0 = "".join(words[0])
    W1 = "".join(words[1])
    W2 = "".join(words[2])
    W3 = [hex(int(word[:4], 2))[2:] + hex(int(word[4:], 2))[2:] for word in words[3]]
    print(f"W{three + 1} = W{zero} ⊕ g(W{three})")
    print(f"W{three} = ", W3)
    X_ = W3[1:] + W3[0:1]
    print(f"X{round_no} = ", X_)

    Y_ = [s_box[i] for i in X_]
    print(f"Y{round_no} = ", Y_)
    Y_bin = "".join([bin(int(i, 16))[2:].rjust(8, "0") for i in Y_])
    print(f"Y{round_no} =  ", Y_bin)
    print(f"⊕ R{round_no}  ", round_constants[round_no])
    print("".center(40, "—"))

    GW_ = ""
    for i in range(32):
        if Y_bin[i] == round_constants[round_no][i]:
            GW_ = GW_ + "0"
        else:
            GW_ = GW_ + "1"
    print(f"G(W{three})= {GW_}")

    print(f"⊕ W{zero}   {W0}")
    print("".center(40, "—"))
    W4 = ""
    for i in range(32):
        if GW_[i] == W0[i]:
            W4 = W4 + "0"
        else:
            W4 = W4 + "1"
    print(f"W{three + 1} =   {W4}")

    print(f"⊕ W{one}   {W1}")
    print("".center(40, "—"))
    W5 = ""
    for i in range(32):
        if W4[i] == W1[i]:
            W5 = W5 + "0"
        else:
            W5 = W5 + "1"
    print(f"W{three + 2} =   {W5}")

    print(f"⊕ W{two}  ", W2)
    print("".center(40, "—"))
    W6 = ""
    for i in range(32):
        if W5[i] == W2[i]:
            W6 = W6 + "0"
        else:
            W6 = W6 + "1"
    print(f"W{three + 3} =   {W6}")

    W3 = "".join(words[3])
    print(f"⊕ W{three}   {W3}")
    print("".center(40, "—"))
    W7 = ""
    for i in range(32):
        if W6[i] == W3[i]:
            W7 = W7 + "0"
        else:
            W7 = W7 + "1"
    print(f"W{three + 4} =   {W7}\n")

    print(f"W{three + 1} - W{three + 4}\n———————————")
    result = [W4, W5, W6, W7]
    for k, v in enumerate(result):
        v1, v2, v3, v4, v5, v6, v7, v8 = hex(int(v[:4], 2))[2:], hex(int(v[4:8], 2))[2:], hex(int(v[8:12], 2))[2:], hex(
            int(v[12:16], 2))[2:], hex(int(v[16:20], 2))[2:], hex(int(v[20:24], 2))[2:], hex(int(v[24:28], 2))[2:], hex(
            int(v[28:32], 2))[2:]
        print(f"W{k + three + 1}", v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8)
    print("\n")
    result_new = []
    for i in result:
        temp = [i[:8], i[8:16], i[16:24], i[24:32]]
        result_new.append(temp)
    return result_new


print("WELCOME TO THE AES SUB-KEY GENERATOR\n—————————————————————————————————————————————————\n")
key = input("Enter your 16-character key:\n")
# key = "odiAaraHOsicnarF"

# Round 0
print("ROUND 0:")
sub_key0 = default_key(key)

# Round 1
print("ROUND 1:")
sub_key1 = sub_key(1, sub_key0)

# Round 2
print("ROUND 2:")
sub_key2 = sub_key(2, sub_key1)

# Round 3
print("ROUND 3:")
sub_key3 = sub_key(3, sub_key2)

# Round 4
print("ROUND 4:")
sub_key4 = sub_key(4, sub_key3)

# Round 5
print("ROUND 5:")
sub_key5 = sub_key(5, sub_key4)

# Round 6
print("ROUND 6:")
sub_key6 = sub_key(6, sub_key5)

# Round 7
print("ROUND 7:")
sub_key7 = sub_key(7, sub_key6)

# Round 8
print("ROUND 8:")
sub_key8 = sub_key(8, sub_key7)

# Round 9
print("ROUND 9:")
sub_key9 = sub_key(9, sub_key8)

# Round 10
print("ROUND 10:")
sub_key10 = sub_key(10, sub_key9)
