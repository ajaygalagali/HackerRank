n = int(input().strip())

numbers = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

k = 0
count = 0

for i in range(n):
    res = 0
    try:

        for j in range(m):
            res = res + numbers[k]
            k+=1

        k -= m-1

        if res == d:
            count+=1
    except IndexError:
        pass
print(count)
