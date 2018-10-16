n = int(input("Input a natural number: ")) # Do not change this line
count = 0
k = 2
prime = bool
while k<=n:
    while n%k == 0:
        count += 1
        n /= k
    k +=1

if count == 1:
    prime = True
else:
    prime = False

if prime:
    print("Prime")
else:
    print("!Prime")