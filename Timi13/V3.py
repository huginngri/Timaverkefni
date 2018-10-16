def menu_selection():
    print('Menu: ')
    choice = input("add(a), remove(r), find(f): ")
    return choice

def execute_selection(choice, a_dict):
    if choice == 'a':
        add_to_dict(a_dict)
    elif choice == 'r':
        remove_from_dict(a_dict)
    elif choice == 'f':
        find_in_dict(a_dict)
    else:
        print('Invalid choice.')

def add_to_dict(a_dict):
    key = input("Key: ")
    value = input("Value: ")
    if key in a_dict:
        print("Error. Key already exists.")
    else:
        a_dict[key] = value

def remove_from_dict(a_dict):
    key = input("key to remove: ")
    if key in a_dict:
        a_dict.pop(key)
    else:
        print("No such key exists in the dictionary.")

def find_in_dict(a_dict):
    key = input("Key to locate: ")
    if key in a_dict:
        print("Value: ", a_dict[key])
    else:
        print("Key not found.")

def dict_to_tuples(a_dict):
    the_list = []
    for item in a_dict.items():
        the_list.append(item)
    return the_list



# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()