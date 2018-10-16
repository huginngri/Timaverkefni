# Your function definition goes here
n = int(input("Input a position between 1 and 10: "))

def Lina(char):
    if char == 'r':
        n = 1
    elif char == 'l':
        n = -1
    else:
        n = 0

    return n

print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")
b = input("Input your choice: ")
flott = Lina(b)
n += flott
if n>10:
    n = 10
elif n<1:
    n = 1
print("New position is:", n)

while b == 'r' or b == 'l':
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    b = input("Input your choice: ")
    flott = Lina(b)
    n += flott
    if n>10:
        n = 10
    elif n<1:
        n = 1
    print("New position is:", n)



