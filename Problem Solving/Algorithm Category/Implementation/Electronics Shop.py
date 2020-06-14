bnm = input().split()

money = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

usb = list(map(int, input().rstrip().split()))
spent = -1

for i in range(len(keyboards)):
    for j in range(len(usb)):
        temp = keyboards[i] + usb[j]
        if temp > spent and temp <= money:
            spent = temp

print(spent)
