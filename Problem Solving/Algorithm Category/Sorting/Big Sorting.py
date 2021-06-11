# Not passed all cases

n = int(input())

unsorted = []

for _ in range(n):
    unsorted_item = int(input())
    unsorted.append(unsorted_item)

print(unsorted)
unsorted.sort()

print(unsorted)