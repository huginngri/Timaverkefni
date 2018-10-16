top_num = int(input("Input a number between 0 and 999: "))

top_rng = range(top_num)

for t in top_rng:
    k = 0
    l = 0
    m = 0
    if t<10:
            k = t % 10
            if k == t:
                print(t)
    if t>=10 and t < 100:
            k = t % 10
            l = t // 10
            if (l*l + k*k) == t:
                print(t)
    if t>=100 and t < 1000:
            k = t % 10
            l = (t // 10) % 10
            m = t // 100
            if (m*m*m + l*l*l + k*k*k) == t:
                print(t)

            
