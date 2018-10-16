import string
#build_wordlist() function goes here
def build_wordlist(infile):
    listinn = ''
    for words in infile:
        listinn += words
    jaja = []
    listinn = listinn.split()
    for word in listinn:
        jaja.append(word.strip(string.punctuation))
    return jaja

#find_unique() function goes here
def find_unique(word_list):
    new_list = []
    for words in word_list:
        if words not in new_list:
            new_list.append(words)
    return new_list


def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()