arr_count = int(input())

arr = list(map(int, input().rstrip().split()))

arr.reverse()

for i in arr:
    print(i,"", end="")
