#game_of_eights() function goes here
def game_of_eights(a_list):
    k = 0
    b = 0
    for num in a_list:
        try:
            int(num)
        except:
            return "Error. Please enter only integers."
    for nums in a_list:
            b = k
            k = int(nums)
            if k == 8 and b == 8:
                return True
    return False
            

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    res = game_of_eights(a_list)
    print(res)

main()