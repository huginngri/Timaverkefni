stars = int(input("Max number of stars: ")) # Do not change this line

s_rng = range(1,stars+1)

for t in s_rng:
    b = range(1,t+1)
    for t in b:
        print("*", end="")
    print()

s_rng2 = range(1,stars)  
for c in s_rng2:
    s = range(c, stars)
    for c in s:
         print("*", end="")
    print()



    
