d = 4
arr = [1 ,2 ,3 ,4 ,5]


for i in range(d):

    temp = arr.pop(0)
    arr.append(temp)

print(arr)