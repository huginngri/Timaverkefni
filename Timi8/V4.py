# Here is the definition of safe_input. It should contain this exception:
def safe_input(prompt, a_type):
    while:
        try:
            tegund = a_type(input(prompt))
            break
        except ValueError:
            print("Error: please enter a value of ", a_type)
    return tegund

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))

