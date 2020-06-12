t = int(input())
for i in range(t):

    num = str(input())

    count = 0
    for i in num:
        ii = int(i)
        numm = int(num)
        try:

            if (numm % ii == 0):
                count += 1
        except:
            pass

    print(count)
