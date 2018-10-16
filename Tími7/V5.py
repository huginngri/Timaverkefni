import string

# palindrome function definition goes here
def pali(flottur):
    gamliflottur = flottur.lower()
    bilofl = string.whitespace + string.punctuation
    for char in gamliflottur:
        if char in bilofl:
            gamliflottur = gamliflottur.replace(char, '')
    
    if gamliflottur[::-1] == gamliflottur:
        return flottur + " is a palindrome."
    else:
        return flottur + " is not a palindrome"



in_str = input("Enter a string: ")

# call the function and print out the appropriate message
awns = pali(in_str)

print(awns)