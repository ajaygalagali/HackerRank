n = int(input())

arr = list(map(int, input().rstrip().split()))
arr.sort()
unique = list(set(arr)) 
NoA = [] #Number of Appearance
count = 0
for i in unique:
    NoA.append(arr.count(i))

for i in NoA:

    count +=i//2

print(count)