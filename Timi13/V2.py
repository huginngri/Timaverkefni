import string

def get_word_list(fpointer):
    fwords = ''
    fwords_list = []
    for words in fpointer:
        fwords += words
    fwords_list_1 = fwords.split()
    for words in fwords_list_1:
        words = words.strip(string.punctuation)
        fwords_list.append(words.lower())
    return fwords_list

def word_list_to_counts(word_list):
    the_dict = {}
    for word in word_list:
        if word not in the_dict:
            the_dict[word] = 1
        else:
            the_dict[word] += 1
    return the_dict

def dict_to_tuple(word_count_dict):
    the_list = []
    for item in word_count_dict.items():
        the_list.append(item)
    return the_list


def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()