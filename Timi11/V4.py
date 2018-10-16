def merge_lists(list1, list2):
    list3 = []
    for nums in list1:
        list3.append(nums)
    for numbs in list2:
        if numbs not in list3:
            list3.append(numbs)
    return sorted(list3)

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
