# Passed all test cases


#!/bin/python3

# Complete the caesarCipher function below.

LOWER = 97
UPPER = 65


def caesarCipher(s, k):
    result = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                result+=giveMe(LOWER,i)

            if i.isupper():
                result+=giveMe(UPPER,i)
        else:
            result+=i
    print("Result",result)

def giveMe(lu,c):
    asciiValue = ord(c)
    n = asciiValue - lu
    kAdded = n + (k%26)
    print("kAdded", kAdded)
    if kAdded >= 26:
        kAdded -= 26

    backToAscii = kAdded + lu
    return chr(backToAscii)


if __name__ == '__main__':

    n = int(input())

    s = input()

    k = int(input())

    caesarCipher(s, k)


# lowercase - 97 to 122
# uppercase - 65 to 90