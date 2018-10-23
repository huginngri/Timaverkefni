def main():
    name = input("Enter name: ").lower()
    first_name, last_name = name.split()
    common_letters = common_letters_using_list(first_name, last_name)
    common_letters2 = common_letters_using_sets(first_name, last_name)
    print(common_letters)
    print(common_letters2)

def common_letters_using_list(first_name, last_name):
    common_letter = []
    for letter in first_name:
        if letter in last_name:
            if letter not in common_letter:
                common_letter.append(letter)
    return sorted(common_letter)

def common_letters_using_sets(first_name, last_name):
    common_letters_set = set()
    for letters in first_name:
        if letters in last_name:
            common_letters_set.add(letters)
    return sorted(list(common_letters_set))

main()