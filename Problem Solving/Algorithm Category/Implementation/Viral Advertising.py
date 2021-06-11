day = 3
initial_shared = 5
liked_ppl = 0
total_liked = 0
for i in range(day):
    liked_ppl = initial_shared//2
    total_liked+=liked_ppl
    initial_shared = liked_ppl*3
    print(i,initial_shared,liked_ppl,total_liked)

print(total_liked)