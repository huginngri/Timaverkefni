
# is_float function definition goes here
def is_float(a):

    try:
        float(a)
        return True
    except:
        return False

print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))