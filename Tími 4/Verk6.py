top_num = int(input("Upper number for the range: "))

t_rng = range(1, top_num+1)

for t in t_rng:
    k= 0
    b_rng = range(1, t+1)
    for b in b_rng:
        if (t % b) == 0 and b != t:
            k += b
    if k == t:        
        print(k)