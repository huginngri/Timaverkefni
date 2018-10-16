
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(a_list):
    b_list = [int(x) for x in a_list if (int(x)%2) == 0]
    b=0
    for x in b_list:
        b += x
    return b

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
