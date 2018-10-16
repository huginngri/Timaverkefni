def dict_func(the_dict):
    name = input("Name: ")
    number = input("Number: ")
    the_dict[name] = number




the_dict = {}
while True:
    dict_func(the_dict)
    cont = input("More data (y/n)? ")
    if cont != 'y':
        break
the_list = []
for item in the_dict.items():
    the_list.append(item)
print(sorted(the_list))
