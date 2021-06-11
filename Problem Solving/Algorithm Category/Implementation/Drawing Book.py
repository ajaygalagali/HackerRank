#Incomplete

n = 10
p = 1
front = abs(1-p)
back = abs(n-p)
# print('front',front)
# print('back',back)
if p == 1:
    print(0)
if front > back:
    # print('Back')
    print(back//2)
else:
    # print('Front')
    print((front//2)+1)
# if back < 0:
#     back = 0
# if n == p or p==1:
#     print(0)
# elif front < back:
#     print(front)
# else:
#     print(back)