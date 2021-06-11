def saveThePrisoner(chairs,candy,position):
    res = ((position -1 +candy-1)%chairs+1)
    if(res==0):
        return position
    else:
        return res


t = int(input())
for i in range(t):
    nms = input().split()

    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])

    result = saveThePrisoner(n, m, s)
    print(result)

