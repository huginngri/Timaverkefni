name = input("Input a name: ")

last, first = name.split(", ")

print(first[0].upper() + ". " + last[0].upper() + last[1:])