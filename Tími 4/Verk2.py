m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

m_rng = range(1, m+1)
n_rng = range(1,n+1)
k = 0
for mnums in m_rng:
    if m % mnums == 0 and n % mnums == 0:
        k = mnums

            


print(k)
