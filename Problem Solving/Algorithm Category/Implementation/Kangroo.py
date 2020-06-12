x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])


for i in range(100000):
    x1+=v1
    x2+=v2

    if x1 == x2:
        print("YES")
        break
else:
    print("NO")
