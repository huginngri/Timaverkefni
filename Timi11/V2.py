#sort_list() function goes here
def sort_list(a_list):
    a_list.sort()
    return None

def main():
    #loop to accept integers until a non-digit is entered goes here
    a_list = []
    while True:
        try:
            numb = int(input())
            a_list.append(numb)
        except:
            break
    
    
    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()