num = int(input("Input an int: ")) # Do not change this line
# hér slæ ég inn tölu

n_rng = range(1, num+1)
#bilið nær frá 1 uppí n



for nnums in n_rng:
    n_rng2 = range(1, nnums+1)
    k = 0
    for nnums2 in n_rng2:
        
        k += nnums2

    print(k)

