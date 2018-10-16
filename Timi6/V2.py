s = input("Input a string: ")

s_len = len(s)

s = s[3:s_len+1] + s[0:3]

print(s)