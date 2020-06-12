
n=int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(1,n+1):
    if arr[-i] < arr[-1]:
        print(arr[-i])
        break
