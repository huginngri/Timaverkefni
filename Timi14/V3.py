import string

import operator

def file_translator():
    file_name = input("Enter name of file: ") 
    fwords = ''
    flist = []
    with open(file_name, 'r') as f:
        for words in f:
            fwords += words
        fwords_list_1 = fwords.split()
        for words in fwords_list_1:
            words = words.strip(string.punctuation)
            flist.append(words.lower())
    return flist

def get_two_word_tuple(the_list):
    new_list = []
    for i in range(len(the_list)-2):
        one_tuple = (the_list[i], the_list[i+1])
        new_list.append(one_tuple)
    return new_list

def count_in_dict(new_list):
    the_dict = {}
    for tuples in new_list:
        if tuples not in the_dict:
            the_dict[tuples] = 1
        else:
            the_dict[tuples] +=1
    the_list_sorted = sorted(the_dict.items(), key=operator.itemgetter(1))
    return the_list_sorted



def main():
    the_list = file_translator()
    list_of_tuples = get_two_word_tuple(the_list)
    the_list_sorted = count_in_dict(list_of_tuples)
    print(the_list_sorted[:-11:-1])
    # small_list = get_the_biggest_values(big_dict)

main()