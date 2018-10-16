s = input("Input a string: ")

for index, letter in enumerate(s):
    if s[index].isdigit() == True:
        print(s[index], end="")