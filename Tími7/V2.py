def counter(stri):
    a = 0
    b = 0
    for i in stri:
        if i.isupper():
            a += 1
        elif i.islower():
            b += 1
    return a,b


user_input = input("Enter a string: ")

upper, lower = counter(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)