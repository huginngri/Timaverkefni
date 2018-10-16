n = int(input("Input an int: ")) # Do not change this line

k = n
while k >= 1:
    if (n % k) == 0:
        print(k)
    k -= 1
