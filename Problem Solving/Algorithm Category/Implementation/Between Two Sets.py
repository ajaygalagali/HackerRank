first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

aLen = len(arr)
bLen = len(brr)
count =0

if aLen > bLen:
    maxLen = aLen
else:
    maxLen = bLen

firstNumber = arr[aLen-1]
lastNumber = brr[0]
# firstNumber = arr[0]
# lastNumber = brr[bLen-1]

for i in range(firstNumber,lastNumber+1):
    try:
        # for q, j in range(aLen), range(bLen):
        #     if (i % arr[q] == 0) and (brr[j]%i==0):
        #         print(i)
        #         count.append(i)

        for q in range(aLen):
            if i%arr[q] !=0:
                break
        else:
            for h in range(bLen):
                if brr[h]%i!=0:
                    break
            else:
                count+=1



    except:
        pass
print(count)
