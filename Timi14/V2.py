def get_set():
    a_list = input("Input a list of integers separated with a comma: ").split(',')
    a_set = set()
    for x in a_list:
        a_set.add(int(x))
    return a_set

def choose_option(a_set, b_set):
    print( "1. Intersection\n2. Union\n3. Difference\n4. Quit")
    the_choice = input("Set operation: ")
    return int(the_choice)

def opperation(number, a_set, b_set):
    if number == 1:
        print(a_set.intersection(b_set))
    elif number == 2:
        print(a_set.union(b_set))
    elif number == 3:
        print(a_set.difference(b_set))






def main():
    a_set = get_set()
    b_set = get_set()
    print(a_set)
    print(b_set)
    option = 0
    while option != 4:
        option = choose_option(a_set, b_set)
        if option < 4:
            opperation(option, a_set, b_set)



main()