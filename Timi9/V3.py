def input_vector(lend):
    i=1
    v = []
    for i in range(lend):
        h = float(input("Element no {}: ".format(i+1)))
        v.append(h)
    return(v)

def dot_product(v1, v2):
    h = 0
    b = len(v1)
    for i in range(b):
        h+= v1[i]*v2[i]

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))