# is_prime function definition goes here
def is_prime(prime):
    counter = 0
    for i in range(1,prime+1):
        if prime % i == 0:
            counter += 1
    if counter == 2:
        return str(prime) + " is a prime"
    else:
        return str(prime) + " is not a prime"    

num = int(input("Input an integer greater than 1: "))

awns = is_prime(num)
# Call the function here and print out the appropriate message

print(awns)