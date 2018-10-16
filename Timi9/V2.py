def to_list(string):
    if ',' in string:
        s = string.split(',')
    else:
        s = string.split()
    return s 



the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)