my_int = int(input('Give me an int >= 0: '))

quote = 0
remaining = my_int
bstr=''

if my_int == 0:
    bstr = "0"

while remaining > 0:
    quote = remaining % 2
    remaining = remaining // 2
    bstr = bstr + str(quote)

bstr = bstr[::-1]

print("The binary of", my_int, "is", bstr)