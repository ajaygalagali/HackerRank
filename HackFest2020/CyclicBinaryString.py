import math
def solveMe(s):
    count = 0
    for i in range(lengthS):
        dec = int(s, 2)

        while 1:
            res = dec/2
            if str(res).endswith(".0"):
                count+=1
                dec = res

            else:
                break

        if count==0:
            s = s[-1]+s[:lengthS-1]
        else:
            print(count)
            break

    else:
        print(0)



# Main
s = input()
lengthS = len(s)
solveMe(s)